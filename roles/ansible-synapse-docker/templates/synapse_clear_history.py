import time
import requests
import json
import psycopg2.extras

login='{{synapse_admin_user}}'
password='{{synapse_admin_pass}}'
db_name='synapse'
db_user='synapse'
db_passwd='{{synapse_db_pass}}'
db_host='localhost'
url= 'localhost:8008/_matrix/client/r0/admin/purge_history/'

def get_auth_token(x,y):
    """ Return auth token after login on service
        x - str: login
 y - str: password
 auth_key - str
    """
    auth_url='https://localhost:8448/_matrix/client/r0/login'
    auth_data= {"type":"m.login.password", "user":x, "password":y}
    _data=json.dumps(auth_data)
    auth=requests.post(auth_url,headers={'content-type':'application/json'},data=_data,verify=False)
    json_data = json.loads(auth.text)
    _auth_key=json_data['access_token']
    auth_key='Bearer '+_auth_key
    return auth_key
def get_room_list():
    """ Return room list in array
    """
    cur.execute('SELECT room_id FROM rooms')
    _room_list=cur.fetchall()
    room_list= []
    for row in _room_list:
 row=row[0]
 room_list.append(row)
    return room_list
def get_last_message(x):
    """ Return last message timstamp
 x - str: room id
 message - timestamp
    """ 
    cur.execute('SELECT origin_server_ts FROM events WHERE room_id=%s ORDER BY origin_server_ts DESC LIMIT 1',(x,))
    message=cur.fetchone()
    message=message[0]    
    return message
def make_url_request(x,y,z):
    _url=url+x
    headers= { 'authorization' : z, 'content-type':'application/json'}
    _data={'delete_local_events': True, 'purge_up_to_ts': y }
    data=json.dumps(_data)
    r=requests.post(_url,headers=headers,data=data)
#    print(r.text)

conn=psycopg2.connect(dbname=db_name, user=db_user, password=db_passwd, host=db_host)
cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
auth_key=get_auth_token(login,password)

for row in get_room_list():
    message=get_last_message(row)
    make_url_request(row,message,auth_key)
conn.close()
exit(0)

import socket
import json

#Set up server parameters
PORT=9898

#this address will be used in case we want to run the server and the client each on a container
HOST = socket.gethostbyname('ipc_server_dns_name') 

#this address will be used in case we want to run the server inside a container and the client outside of a container
#HOST=socket.gethostbyname(socket.gethostname()) 

HEADER=64
FORMAT='UTF-8'
ADDR=(HOST,PORT)
DISCONNECT_MESSAGE='Disconnect'


#Set up connection
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

#Set up send function
def send(msg):
    message=msg.encode(FORMAT)
    msg_length=len(message)
    send_length=str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER-len(send_length))
    client.send(send_length)
    client.send(message)

#Set up recieve function
def recieve():
    outcome=client.recv(1024).decode(FORMAT)
    print(outcome)
    
#test coordinates
latitudes = [31.04, 35.15, 44.71]
longitudes = [-20.18, -10.15, 2.41]

#convert to json
data1=json.dumps(latitudes)
data2=json.dumps(longitudes)

send(data1)
send(data2)
send(DISCONNECT_MESSAGE)
recieve()

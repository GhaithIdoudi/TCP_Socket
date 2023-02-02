import socket
import threading
import json
from coordinate_combiner import coordinate_combiner

#Set up server parameters
PORT=9898

#this will be used in case we want to run the server and the client each on a container
#HOST = socket.gethostbyname('ipc_server_dns_name') 

#this address will be used in case we want to run the server inside a container and the client outside of a container
HOST='0.0.0.0'  

ADDR=(HOST,PORT)
HEADER=64
FORMAT='UTF-8'
DISCONNECT_MESSAGE='Disconnect'

#Set up connection
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)


#accept client connection, recieve input and sent back the output
def handle_client(connection,addr):
    connected=True
    coord=[]
    while connected:
        msg_length=connection.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length=int(msg_length)
            msg=connection.recv(msg_length).decode(FORMAT)
            if msg==DISCONNECT_MESSAGE:
                connected=False
            else:
                coord.append(msg)
            
                

    latitudes=coord[0]
    latitudes=latitudes[1:-1]
    latitudes=latitudes.split(',')
    latitudes=[float(x) for x in latitudes]
    longitudes=coord[1]
    longitudes=longitudes[1:-1]
    longitudes=longitudes.split(',')
    longitudes=[float(y) for y in longitudes]
    result=coordinate_combiner(latitudes,longitudes)
    result=json.dumps(result)
    connection.send(result.encode(FORMAT))
    connection.close()

#Start server
def start():
    server.listen()
    while True:
        connection, addr=server.accept()
        thread=threading.Thread(target=handle_client, args=(connection,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() -1}")


print('Server is starting')
print(f'Server is listenning on {ADDR}')
start()

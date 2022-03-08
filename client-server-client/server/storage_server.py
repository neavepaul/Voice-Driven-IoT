from time import sleep
import socket
import pickle
from _thread import *

host = ''
port = 7052

HEADERSIZE = 10
ACTIVE_CONNS = 0


stored_value = {'R_LED':0, 'Y_LED':0, 'W_LED':0, 'B_LED':0, 'BUZZER_1':0, 'BUZZER_5':0, 'DISPLAY':'', 'KILL': 0}

def setup_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Socket created.")
    try:
        s.bind((host, port))
    except socket.error as error:
        print(error)
    print("Socket bind completed.")
    return s

def setup_connection():
    s.listen(5) 
    conn, addr = s.accept()
    print("Connected to:"+addr[0]+":"+str(addr[1]))
    return conn

def UPDATE():
    return stored_value


def data_transfer(conn):
    global KILL
    # send and receives data until told otherwise
    while True:
    
            # receive data
            full_msg = b''
            new_msg = True
            msg = 'SOME UN-RECOGNIZED SHIT'
            msg = conn.recv(1024)#buffer size
            if new_msg:
                msglen = int(msg[:HEADERSIZE])
                new_msg = False
            full_msg += msg
            if len(full_msg)-HEADERSIZE == msglen:
                commander = pickle.loads(full_msg[HEADERSIZE:])


                if type(commander) is dict:
                    stored_value.update(commander)
                    print("new stored values")
                    print(stored_value)


                    reply = "Values updated in server storage"
                    conn.sendall(str.encode(reply))
                    continue
                elif commander == "UPDATE":
                    reply = UPDATE()
                elif commander == 'KILL':
                    print("Shutting down Neptune Server")
                    stored_value.update({'KILL': 1})
                    s.close()
                    exit("killed...")
                    break
                elif commander == "EXIT":
                    print("Sad to see you leave :(")
                    break
                else:
                    print("I GOT SOME UN-RECOGNIZED SHIT.")

                msg = pickle.dumps(reply, -1)
                msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
                conn.sendall(msg)
                stored_value.update({'DISPLAY':'', 'BUZZER_1':0, 'BUZZER_5':0})
                new_msg = True
                full_msg = b''

                print("Requested action completed")


    conn.close()

            
s = setup_server()

while True:
    try:
        conn = setup_connection()
        
        start_new_thread(data_transfer, (conn, ))
        ACTIVE_CONNS+=1
        print("Active clients: "+str(ACTIVE_CONNS))
        
    except:
        break
    




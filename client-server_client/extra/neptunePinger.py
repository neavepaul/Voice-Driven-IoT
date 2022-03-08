#to check server status via cli
import socket

host = ''
port = 7052

stored_value = "Hey! I am the Neptune Server"

def setup_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    try:
        s.bind((host, port))
    except socket.error as error:
        print(error)
    print("Socket bind completed.")
    return s

def setup_connection():
    s.listen(1) #the other pi
    conn, addr = s.accept()
    print("Connected to:"+addr[0]+":"+str(addr[1]))
    return conn

def GET():
    return stored_value

def REPEAT(data_message):
    return data_message[1]

def data_transfer(conn):
    # send and receives data until told otherwise
    while True:
        # receive data
        data = conn.recv(1024)#buffer size
        data = data.decode('utf-8')
        data_message = data.split(' ',1)
        command_type = data_message[0]
        if command_type == "GET":
            reply = GET()
        elif command_type == "REPEAT":
            reply = REPEAT(data_message)
        elif command_type == "GPIO":
            pass
        elif command_type == "EXIT":
            print("Sad to see you leave :(")
            break
        elif command_type == "KILL":
            print("Shutting down Neptune Server")
            s.close()
            break
        else:
            print("Unknown command.")
        
        #send the ata back to the client
        conn.sendall(str.encode(reply))
        print("Data has been sent to client")
    conn.close()

            
s = setup_server()

while True:
    try:
        conn = setup_connection()
        data_transfer(conn)
    except:
        break
    

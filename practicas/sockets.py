import socket              # Import socket module
import threading

h_name = socket.gethostname()
IP_addres = socket.gethostbyname(h_name)
print("Host Name is:", h_name)
print("Computer IP Address is:", IP_addres)

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50008              # Arbitrary non-privileged port

def on_new_client(conn,addr):
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if data:
            print('Received: ', repr(data))
        msg = input("Ingrese un mensaje: ")
        conn.sendall(msg.encode())
        conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    
    s.listen(10)
    while True:
        conn, addr = s.accept()
        #threading.Thread(target=on_new_client, args=(conn,addr))
        while True:
            data = conn.recv(1024)
            if data:
                print('Received: ', repr(data))
            msg = input("Ingrese un mensaje: ")
            conn.sendall(msg.encode())

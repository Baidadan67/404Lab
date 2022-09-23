#!/usr/bin/env python3
from multiprocessing import Process
import socket, sys
import time

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    print (f'Ip address of {host} is {remote_ip}')
    return remote_ip


    
def main():
    host = "www.google.com"
    port = 80
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as start:
    
        #QUESTION 3
        start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        start.bind((HOST, PORT))
        #set to listening mode
        start.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = start.accept()
            print("Connected by", addr)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as end:
                remote_ip = get_remote_ip(host)
                end.connect((remote_ip, port))
                p = Process(target=handle_echo, args=(end, addr, conn))
            full_data = conn.recv(BUFFER_SIZE)
            time.sleep(0.5)
            conn.sendall(full_data)
            conn.close()

def handle_echo(end, addr, conn):
    full_data = conn.recv(BUFFER_SIZE)
    end.sendall(full_data)
    end.shutdown(socket.SHUT_WR)
    d = end.recv(BUFFER_SIZE)
    conn.send(d)

if __name__ == "__main__":
    main()

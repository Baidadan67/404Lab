#!/usr/bin/env python3

import socket, sys

HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024
payload = "GET / HTTP/1.0\r\nhost: www.google.com\r\n"
addr = '127.0.0.1'
#create a tcp socket
'''def create_tcp_socket():
    print('Creating socket')
    try:
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(addr)
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)
    except Exception as e:
        print(e)
    finally:
        s.close()   
        
    return s
    '''

#get host information
"""
def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    print (f'Ip address of {host} is {remote_ip}')
    return remote_ip
    

#send data to server
def send_data(serversocket, payload):
    print("Sending payload")    
    try:
        serversocket.sendall(payload.encode())
    except socket.error:
        print ('Send failed')
        sys.exit()
    print("Payload sent successfully")
    """
def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((addr,PORT))
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)
    except Exception as e:
        print(e)
    finally:
        s.close()  

       

if __name__ == "__main__":
    main()


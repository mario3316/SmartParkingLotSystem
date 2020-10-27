import serial
import socket
import time
import pickle
import sys

if __name__ == "__main__":
    PORT = int(sys.argv[1])
    my_id = sys.argv[2]

# Set Port , Baud Rate
serial_PORT = 'COM5'
BaudRate = 9600
ARD = serial.Serial(serial_PORT, BaudRate)

print('serial' + serial.__version__)
value = []

def setting():
    global PORT, my_id
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP = '192.168.57.1'
    client_socket.connect((IP, PORT))
    data = pickle.dumps(my_id)
    client_socket.send(data)

    return client_socket


def sendData(client_socket, value):
    data = pickle.dumps(value)
    client_socket.send(data)

def Decode(A):
    A = A.decode()
    A = str(A)
    temp = A.strip('[]').replace(']\r\n', '').split(',')
    temp = list(map(int, temp))
    return temp

def Ardread() :
    if ARD.readable():
        line = ARD.readline()
        value = Decode(line)
        del value[1]
        sendData(client_socket, value)
        print(value)
        ARD.flush()
    else:
        print("Failed to read from Arduino")

client_socket = setting()

while(True):
    try:
        Ardread()
        time.sleep(0.5)
    except KeyboardInterrupt:
        data = pickle.dumps("quit")
        client_socket.send(data)
        raise
import socket
import time
import pickle
import threading
import random
import sys

if __name__ == "__main__":
    PORT = int(sys.argv[1])
    my_id = sys.argv[2]


value = [1,2,3,4,5]
threads = []


def setting():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP = '192.168.57.1'
    #PORT = int(input('Port : '))
    #my_id = input('Floor : ')
    client_socket.connect((IP, PORT))
    data = pickle.dumps(my_id)
    client_socket.send(data)

    return client_socket


def sendData(client_socket, value):
    data = pickle.dumps(value)
    client_socket.send(data)

def random_generate():
    global value
    while(True):
        for t in range(0, 5):
            value[t] = random.randint(1, 15)
        time.sleep(120) #60초에 한번씩 랜덤값 생성

def main():
    while (True):
        try:
            sendData(client_socket, value)
            print(value)
            time.sleep(0.5)
        except KeyboardInterrupt:
            data = pickle.dumps("quit")
            client_socket.send(data)
            raise


client_socket = setting()
newthread = threading.Thread(target=random_generate)
newthread.start()
threads.append(newthread)

newthread = threading.Thread(target=main)
newthread.start()
threads.append(newthread)

for t in threads:
    t.join()


import socket
import threading
import pickle
import sys
from datetime import datetime

if __name__ == "__main__":
    port = int(sys.argv[1])
    location = sys.argv[2]
    floor_num = int(sys.argv[3])

client_id = []
threads = []
num = 0
dict = {}

def sender(client_socket, value):
    data = pickle.dumps(value)
    client_socket.send(data)

def receiver(client_socket):
    data = client_socket.recv(1024)
    recv_data = pickle.loads(data)
    return recv_data

def print_current():
    print("Current Client : ", client_id)

def Decode(A):
    A = A.decode()
    A = str(A)
    temp = A.strip('[]').replace(']\r\n', '').split(',')
    temp = list(map(int, temp))
    return temp

def handler(client_socket, my_num, id):
    print(id)
    f = open(location + "_" + id +".txt", 'w')

    while True:
        try:
            global num
            rcvData = receiver(client_socket)
            rcvStr = ', '.join(str(e) for e in rcvData)
            print_current()

            if rcvData == "quit":
                print("ID : %s  Disconnected" % id)
                client_id.remove(id)
                num = num - 1
                client_socket.close()
                f.close()
                return
            else:
                dict = {'location': location, 'Floor': id}
                for i in range(0, 5):
                    if rcvData[i] < 5 and rcvData[i] != 0:
                        dict[i] = 1
                    else:
                        dict[i] = 0     #주차 가능 : 0 , 주차 불가능 : 1
                print(dict)
                sender(main_server_socket, dict)

                s = (datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "  [" + rcvStr + "]")
                print(s)
                f.write(s)
                f.write("\n")
        except:
            print("ID : %s  Disconnected" % id)
            client_id.remove(id)
            num = num - 1
            client_socket.close()
            f.close()
            return

server_ip = socket.gethostbyname(socket.getfqdn())
print('My IP : '+ server_ip)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, port))

main_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_server_socket.connect(('192.168.57.1', 9999))
sender(main_server_socket, location)
print(receiver(main_server_socket))
sender(main_server_socket,floor_num)

while True:
    server_socket.listen(4)
    print('%d Port is Listening...' % port)
    client_socket, addr = server_socket.accept()
    client_id.append(receiver(client_socket))
    print(client_id[num], "has connected.")
    my_num = num
    num = num+1

    newthread = threading.Thread(target=handler, args = (client_socket, my_num, client_id[my_num]))
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()
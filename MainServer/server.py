import socket
import threading
import pickle
import time
from datetime import datetime

parkinglot_id = []
client_id = []
parkinglot_threads = []
client_threads = []
parkinglot_num = 0
client_num = 0

singong = [{'location':'singong','Floor':'B1', 0: 0, 1: 0, 2: 0, 3: 0, 4: 0},
           {'location':'singong','Floor':'B2', 0: 0, 1: 0, 2: 0, 3: 0, 4: 0},
           {'location':'singong','Floor':'B3', 0: 0, 1: 0, 2: 0, 3: 0, 4: 0},
           {'location':'singong','Floor':'B4', 0: 0, 1: 0, 2: 0, 3: 0, 4: 0}]
gongdae = [{'location':'gongdae','Floor':'B1', 0: 0, 1: 0, 2: 0, 3: 0, 4: 0},
           {'location':'gongdae','Floor':'B2', 0: 0, 1: 0, 2: 0, 3: 0, 4: 0},
           {'location':'gongdae','Floor':'B3', 0: 0, 1: 0, 2: 0, 3: 0, 4: 0}]
sanhak = [{'location':'sanhak','Floor':'B1', 0: 0, 1: 0, 2: 0, 3: 0, 4: 0},
          {'location':'sanhak','Floor':'B2', 0: 0, 1: 0, 2: 0, 3: 0, 4: 0},
          {'location':'sanhak','Floor':'B3', 0: 0, 1: 0, 2: 0, 3: 0, 4: 0},
          {'location':'sanhak','Floor':'B4', 0: 0, 1: 0, 2: 0, 3: 0, 4: 0}]
haebong = [{'location':'haebong','Floor':'B1', 0: 0, 1: 0, 2: 0, 3: 0, 4: 0},
           {'location':'haebong','Floor':'B2', 0: 0, 1: 0, 2: 0, 3: 0, 4: 0}]  #4개 주차장 설정

port_parkinglot = 9999
port_client = 8888
port_admin = 7777

server_ip = socket.gethostbyname(socket.getfqdn())
print('Welcome to Konkuk University Smart Parking Lot System ('+ server_ip + ')')

def update_info(dict,f):
    s = (datetime.now().strftime('%Y-%m-%d %H:%M:%S') + str(dict))
    if dict.get('location') == 'singong':
        if dict.get('Floor') == 'B1':
            singong[0] = dict
            f[0].write(s)
            f[0].write("\n")
        elif dict.get('Floor') == 'B2':
            singong[1] = dict
            f[1].write(s)
            f[1].write("\n")
        elif dict.get('Floor') == 'B3':
            singong[2] = dict
            f[2].write(s)
            f[2].write("\n")
        elif dict.get('Floor') == 'B4':
            singong[3] = dict
            f[3].write(s)
            f[3].write("\n")
    elif dict.get('location') == 'gongdae':
        if dict.get('Floor') == 'B1':
            gongdae[0] = dict
            f[0].write(s)
            f[0].write("\n")
        elif dict.get('Floor') == 'B2':
            gongdae[1] = dict
            f[1].write(s)
            f[1].write("\n")
        elif dict.get('Floor') == 'B3':
            gongdae[2] = dict
            f[2].write(s)
            f[2].write("\n")
    elif dict.get('location') == 'sanhak':
        if dict.get('Floor') == 'B1':
            sanhak[0] = dict
            f[0].write(s)
            f[0].write("\n")
        elif dict.get('Floor') == 'B2':
            sanhak[1] = dict
            f[1].write(s)
            f[1].write("\n")
        elif dict.get('Floor') == 'B3':
            sanhak[2] = dict
            f[2].write(s)
            f[2].write("\n")
        elif dict.get('Floor') == 'B4':
            sanhak[3] = dict
            f[3].write(s)
            f[3].write("\n")
    elif dict.get('location') == 'haebong':
        if dict.get('Floor') == 'B1':
            haebong[0] = dict
            f[0].write(s)
            f[0].write("\n")
        elif dict.get('Floor') == 'B2':
            haebong[1] = dict
            f[0].write(s)
            f[0].write("\n")

def sender(socket, value):
    data = pickle.dumps(value)
    socket.send(data)

def receiver(client_socket):
    try:
        data = client_socket.recv(1024)
        recv_data = pickle.loads(data)
        return recv_data
    except EOFError:
        return

def print_current():
    print("Current Client : ", client_id)

def book_init(location, floor, num):
    max_time_end = time.time() + 15
    while(True):
        if time.time() < max_time_end:
            if location == "singong":
                singong[int(floor[1])-1][num] = 1
            elif location == "gongdae":
                gongdae[int(floor[1]) - 1][num] = 1
            if location == "sanhak":
                sanhak[int(floor[1]) - 1][num] = 1
            if location == "haebong":
                haebong[int(floor[1]) - 1][num] = 1
        else:
            break

    if location == "singong":
        singong[int(floor[1]) - 1][num] = 0
    elif location == "gongdae":
        gongdae[int(floor[1]) - 1][num] = 0
    if location == "sanhak":
        sanhak[int(floor[1]) - 1][num] = 0
    if location == "haebong":
        haebong[int(floor[1]) - 1][num] = 0
    print(location, " ", floor, " ", str(num), " 예약 끝")

def parkinglot_handler(client_socket, location, id, floor_num):
    global parkinglot_num
    global parkinglot_id
    f = []

    for i in range(0, floor_num):
        f.append(open(location + "_B" + str(i + 1) + ".txt", 'a'))

    while True:
        try:
            rcvData = receiver(client_socket)
            dict = rcvData
            if rcvData == "quit":
                print("ID : %s  Disconnected" % id)
                parkinglot_id.remove(location)
                parkinglot_num = parkinglot_num - 1
                client_socket.close()
                for i in range(0, floor_num):
                    f[i].close()
                return
            else:
                update_info(dict, f)

        except:
            print("[Parking Lot] %s  Disconnected" % location)
            parkinglot_id.remove(location)
            parkinglot_num = parkinglot_num - 1
            client_socket.close()
            for i in range(0, floor_num):
                if f[i].closed == False :
                    f[i].close()
            return

def client_handler(client_socket, id):
    global client_num
    global client_id

    while True:
        try:
            rcvData = receiver(client_socket)
            if rcvData == "quit":
                print("ID : %s  Disconnected" % id)
                client_id.remove(id)
                client_num = client_num - 1
                client_socket.close()
                return
            elif rcvData == "singong":
                sender(client_socket, singong)
            elif rcvData == "gongdae":
                sender(client_socket, gongdae)
            elif rcvData == "sanhak":
                sender(client_socket, sanhak)
            elif rcvData == "haebong":
                sender(client_socket, haebong)
            elif rcvData == "book":
                book_data = receiver(client_socket)
                book_location = book_data[0]
                book_floor = book_data[1]
                book_num = book_data[2]
                if book_location == 'singong':
                    singong[int(book_floor[1])-1][book_num] = 1
                    print("신공학관", book_floor, "층 ", str(book_num), "번 예약완료")
                    book_thread = threading.Thread(target=book_init, args=(book_location, book_floor, book_num))
                    book_thread.start()
                elif book_location == 'gongdae':
                    gongdae[int(book_floor[1])-1][book_num] = 1
                    print("공과대학 ", book_floor, "층 ", str(book_num), "번 예약완료")
                    book_thread = threading.Thread(target=book_init, args=(book_location, book_floor, book_num))
                    book_thread.start()
                elif book_location == 'sanhak':
                    sanhak[int(book_floor[1]) - 1][book_num] = 1
                    print("산학협동관 ", book_floor, "층 ", str(book_num), "번 예약완료")
                    book_thread = threading.Thread(target=book_init, args=(book_location, book_floor, book_num))
                    book_thread.start()
                elif book_location == 'haebong':
                    haebong[int(book_floor[1])-1][book_num] = 1
                    print("해봉관 ", book_floor, "층 ", str(book_num), "번 예약완료")
                    book_thread = threading.Thread(target=book_init, args=(book_location, book_floor, book_num))
                    book_thread.start()
            elif rcvData == "list":
                total = list()
                total.append(singong)
                total.append(gongdae)
                total.append(sanhak)
                total.append(haebong)
                sender(client_socket, total)

        except:
            print("[Client] %d  Disconnected" % id)
            client_id.remove(id)
            client_num = client_num - 1
            client_socket.close()
            return

def send_log(target_socket):
    global client_num#, target_socket
    while(True):
        try:
            send_list = ["", ""]
            str_list = ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]
            for i in range(0, 4):
                str_list[i] = str(singong[i])
            for i in range(0, 3):
                str_list[i+4] = str(gongdae[i])
            for i in range(0, 4):
                str_list[i+7] = str(sanhak[i])
            for i in range(0, 2):
                str_list[i+11] = str(haebong[i])
            send_list[0] = str_list
            send_list[1] = client_id
            sender(target_socket, send_list)
            time.sleep(0.5)
        except:
            print("Admin Disconnected")
            target_socket.close()
            return

def parkinglot():
    parkinglot_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    parkinglot_socket.bind((server_ip, port_parkinglot))

    global parkinglot_id
    global parkinglot_threads
    global parkinglot_num

    while(True):
        parkinglot_socket.listen(4)  # 4개 주차장
        parkinglot_client_socket, parkinglot_addr = parkinglot_socket.accept()

        parkinglot_id.append(receiver(parkinglot_client_socket))
        sender(parkinglot_client_socket,"Welcome to main server")
        floor_num = receiver(parkinglot_client_socket)
        print("[Parking Lot] ", parkinglot_id[parkinglot_num], "has connected.[Floor num] : " , floor_num)
        id = parkinglot_num
        parkinglot_num = parkinglot_num+1

        newthread = threading.Thread(target=parkinglot_handler, args=(parkinglot_client_socket, parkinglot_id[id], id, floor_num))
        newthread.start()
        parkinglot_threads.append(newthread)

    for t in parkinglot_threads:
        t.join()

def client():
    for_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for_client_socket.bind((server_ip, port_client))

    global client_id
    global client_threads
    global client_num

    while(True):
        for_client_socket.listen()
        client_client_socket, client_addr = for_client_socket.accept()
        sender(client_client_socket, "Welcome to Konkuk University Smart Parking Lot System")
        client_id.append(receiver(client_client_socket))
        print("[Client] ", client_id[client_num], "has connected.")
        my_num = client_num
        client_num = client_num + 1

        newthread = threading.Thread(target=client_handler, args = (client_client_socket, client_id[my_num]))
        newthread.start()
        client_threads.append(newthread)

    for t in client_threads:
      t.join()

def admin():
    global target_socket
    for_admin_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for_admin_socket.bind((server_ip, port_admin))

    while (True):
        for_admin_socket.listen()
        admin_client_socket, admin_addr = for_admin_socket.accept()

        sender(admin_client_socket, "Please Enter PassWord : ")
        if receiver(admin_client_socket) != "2019np":
            sender(admin_client_socket, "no")
            # for_admin_socket.close()
        else :
            sender(admin_client_socket, "yes")
            print("Admin has connected.")
            log_thread = threading.Thread(target=send_log, args=(admin_client_socket,))
            log_thread.start()

pl_thread = threading.Thread(target = parkinglot)
cl_thread = threading.Thread(target = client)
ad_thread = threading.Thread(target = admin)
pl_thread.start()
cl_thread.start()
ad_thread.start()
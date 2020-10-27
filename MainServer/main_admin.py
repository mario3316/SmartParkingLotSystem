import pickle
import socket
import sys
import time
import threading
from datetime import datetime

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import admin
import admin_main

IP = '192.168.57.1'
PORT = 7777
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rcv_list = []
count = 0

class MainWindow(QMainWindow):
    sig = pyqtSignal()

    def __init__(self):
        super(MainWindow, self).__init__()

        # UI 객체 생성
        self.adminUI = admin.adminUI()
        self.admin_mainUI = admin_main.admin_mainUI()
        self.adminUI.show()  # 최초에 로그인 UI 보이기

        # 창 전환 관련 이벤트 슬롯 매칭
        self.adminUI.pushButton.clicked.connect(self.check_pw)
        self.admin_mainUI.pushButton_admin_main_back.clicked.connect(self.click_back)

        self.sig.connect(self.update_ui)

    def update_ui(self):
        s = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for i in range(0, 13):
            self.admin_mainUI.textBrowser_admin_main_log.append(s + str(rcv_list[0][i]) + '\n')

        self.admin_mainUI.textBrowser_admin_main_log_2.setText(str(rcv_list[1]))

    def print_log(self):
        global rcv_list
        while True:
            try:
                time.sleep(0.5)
                rcv_list = self.receiver(client_socket)
                self.sig.emit()
                QApplication.processEvents(QEventLoop.ExcludeUserInputEvents)
            except:
                print("로그 출력 쓰레드 종료!")
                return

    def check_pw(self):
        global count
        global client_socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((IP, PORT))
        print(self.receiver(client_socket))
        password = self.adminUI.textEdit_admin.toPlainText()  # 패스워드 : 2019np
        if len(password) > 30:
            QMessageBox.about(self, 'System', 'Password too long!')
        else:
            self.sender(client_socket, password)
            if self.receiver(client_socket) == "yes": # 접속 성공
                QMessageBox.about(self, 'System', '접속에 성공하였습니다')
                self.admin_mainUI.show()
                t = threading.Thread(target=self.print_log)
                t.start()
                self.adminUI.close()
            else: # 접속 실패
                QMessageBox.about(self, 'System', '패스워드 미일치')
                client_socket.close()

    def click_back(self):
        self.adminUI.show()
        self.admin_mainUI.close()
        self.adminUI.close()
        client_socket.close()

    def sender(self, client_socket, value):
        data = pickle.dumps(value)
        client_socket.send(data)

    def receiver(self, client_socket):
        data = client_socket.recv(10240)
        recv_data = pickle.loads(data)
        return recv_data


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
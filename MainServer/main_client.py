import pickle
import socket
import sys

import random
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import main
import check
import check_gongdae
import check_singong
import check_sanhak
import check_haebong
import book
import book_singong
import book_gongdae
import book_sanhak
import book_haebong
import ask

my_id = random.randint(1,10000)
blue_brush = QBrush(QColor(0, 0, 255))
blue_brush.setStyle(Qt.SolidPattern)
red_brush = QBrush(QColor(255, 0, 0))
red_brush.setStyle(Qt.SolidPattern)

location = 'singong'
book_floor = 'B1'
book_num = 0
item = []

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # 로그인 서버에 연결 요청
        self.client_socket = self.setting()

        # UI 객체 생성
        self.mainUI = main.mainUI()
        self.askUI = ask.askUI()
        self.checkUI = check.checkUI()
        self.check_singongUI = check_singong.check_singongUI()
        self.check_gongdaeUI = check_gongdae.check_gongdaeUI()
        self.check_sanhakUI = check_sanhak.check_sanhakUI()
        self.check_haebongUI = check_haebong.check_haebongUI()

        self.bookUI = book.bookUI()
        self.book_singongUI = book_singong.book_singongUI()
        self.book_gongdaeUI = book_gongdae.book_gongdaeUI()
        self.book_sanhakUI = book_sanhak.book_sanhakUI()
        self.book_haebongUI = book_haebong.book_haebongUI()

        self.mainUI.label_printID.setText("ID : " + str(my_id))


        self.mainUI.show()  # 최초에 로그인 UI 보이기

        # 커스텀 시그널 객체 생성
        # self.signal = CustomSignals()

        # 창 전환 관련 이벤트 슬롯 매칭
        self.mainUI.pushButton_check.clicked.connect(self.click_check)
        self.mainUI.pushButton_book.clicked.connect(self.click_book)

        # 조회 버튼 클릭시
        self.checkUI.pushButton_check_back.clicked.connect(self.click_back)
        self.checkUI.pushButton_check_singong.clicked.connect(self.click_check_singong)
        self.checkUI.pushButton_check_gongdae.clicked.connect(self.click_check_gongdae)
        self.checkUI.pushButton_check_sanhak.clicked.connect(self.click_check_sanhak)
        self.checkUI.pushButton_check_haebong.clicked.connect(self.click_check_haebong)

        # 조회 버튼에서 주차장 클릭시
        self.check_singongUI.pushButton_show_singong_back.clicked.connect(self.click_check_back)
        self.check_gongdaeUI.pushButton_show_gongdae_back.clicked.connect(self.click_check_back)
        self.check_sanhakUI.pushButton_show_sanhak_back.clicked.connect(self.click_check_back)
        self.check_haebongUI.pushButton_show_haebong_back.clicked.connect(self.click_check_back)

        # 예약 버튼 클릭시
        self.bookUI.pushButton_book_back.clicked.connect(self.click_back)
        self.bookUI.pushButton_book_singong.clicked.connect(self.click_book_singong)
        self.bookUI.pushButton_book_gongdae.clicked.connect(self.click_book_gongdae)
        self.bookUI.pushButton_book_sanhak.clicked.connect(self.click_book_sanhak)
        self.bookUI.pushButton_book_haebong.clicked.connect(self.click_book_haebong)

        # 예약에서 주차장 클릭시
        self.book_singongUI.pushButton_book_singong_back.clicked.connect(self.click_book_back)
        self.book_gongdaeUI.pushButton_book_gongdae_back.clicked.connect(self.click_book_back)
        self.book_sanhakUI.pushButton_book_sanhak_back.clicked.connect(self.click_book_back)
        self.book_haebongUI.pushButton_book_haebong_back.clicked.connect(self.click_book_back)

        # 예약하려는 주차장 좌석 더블 클릭시
        self.book_singongUI.listWidget_book_B1_singong.itemDoubleClicked.connect(self.click_book_singong_B1)
        self.book_singongUI.listWidget_book_B2_singong.itemDoubleClicked.connect(self.click_book_singong_B2)
        self.book_singongUI.listWidget_book_B3_singong.itemDoubleClicked.connect(self.click_book_singong_B3)
        self.book_singongUI.listWidget_book_B4_singong.itemDoubleClicked.connect(self.click_book_singong_B4)

        self.book_gongdaeUI.listWidget_book_B1_gongdae.itemDoubleClicked.connect(self.click_book_gongdae_B1)
        self.book_gongdaeUI.listWidget_book_B2_gongdae.itemDoubleClicked.connect(self.click_book_gongdae_B2)
        self.book_gongdaeUI.listWidget_book_B3_gongdae.itemDoubleClicked.connect(self.click_book_gongdae_B3)

        self.book_sanhakUI.listWidget_book_B1_sanhak.itemDoubleClicked.connect(self.click_book_sanhak_B1)
        self.book_sanhakUI.listWidget_book_B2_sanhak.itemDoubleClicked.connect(self.click_book_sanhak_B2)
        self.book_sanhakUI.listWidget_book_B3_sanhak.itemDoubleClicked.connect(self.click_book_sanhak_B3)
        self.book_sanhakUI.listWidget_book_B4_sanhak.itemDoubleClicked.connect(self.click_book_sanhak_B4)

        self.book_haebongUI.listWidget_book_B1_haebong.itemDoubleClicked.connect(self.click_book_haebong_B1)
        self.book_haebongUI.listWidget_book_B2_haebong.itemDoubleClicked.connect(self.click_book_haebong_B2)


        self.askUI.pushButton_ask_no.clicked.connect(self.ask_no)
        self.askUI.pushButton_ask_yes.clicked.connect(self.ask_yes)

    def ask_no(self):
        QMessageBox.about(self, 'System', '취소되었습니다')
        self.askUI.close()

    def ask_yes(self):
        global item
        self.sender(self.client_socket, "book")
        self.sender(self.client_socket, (location, book_floor, book_num))
        QMessageBox.about(self, 'System', '예약 되었습니다. 15초 내에 미주차시 취소됩니다')
        item.setBackground(red_brush)
        self.askUI.close()

    def click_book_singong_B1(self):
        global location, book_floor, book_num, item

        row = self.book_singongUI.listWidget_book_B1_singong.currentRow()

        self.sender(self.client_socket, "singong")
        singong = self.receiver(self.client_socket)
        disable = self.getKeysByValue(singong[0], 1)
        if row in disable:
            QMessageBox.about(self, 'System', '예약 할 수 없는 자리입니다.')
            return

        location = "singong"
        book_floor = 'B1'
        book_num = row
        item = self.book_singongUI.listWidget_book_B1_singong.currentItem()
        self.askUI.show()

    def click_book_singong_B2(self):
        global location, book_floor, book_num, item

        row = self.book_singongUI.listWidget_book_B2_singong.currentRow()

        self.sender(self.client_socket, "singong")
        singong = self.receiver(self.client_socket)
        disable = self.getKeysByValue(singong[0], 1)
        if row in disable:
            QMessageBox.about(self, 'System', '예약 할 수 없는 자리입니다.')
            return

        location = "singong"
        book_floor = 'B2'
        book_num = row
        item = self.book_singongUI.listWidget_book_B2_singong.currentItem()
        self.askUI.show()

    def click_book_singong_B3(self):
        global location, book_floor, book_num, item

        row = self.book_singongUI.listWidget_book_B3_singong.currentRow()

        self.sender(self.client_socket, "singong")
        singong = self.receiver(self.client_socket)
        disable = self.getKeysByValue(singong[0], 1)
        if row in disable:
            QMessageBox.about(self, 'System', '예약 할 수 없는 자리입니다.')
            return

        location = "singong"
        book_floor = 'B3'
        book_num = row
        item = self.book_singongUI.listWidget_book_B3_singong.currentItem()
        self.askUI.show()

    def click_book_singong_B4(self):
        global location, book_floor, book_num, item

        row = self.book_singongUI.listWidget_book_B4_singong.currentRow()

        self.sender(self.client_socket, "singong")
        singong = self.receiver(self.client_socket)
        disable = self.getKeysByValue(singong[0], 1)
        if row in disable:
            QMessageBox.about(self, 'System', '예약 할 수 없는 자리입니다.')
            return

        location = "singong"
        book_floor = 'B4'
        book_num = row
        item = self.book_singongUI.listWidget_book_B4_singong.currentItem()
        self.askUI.show()

    def click_book_gongdae_B1(self):
        global location, book_floor, book_num, item

        row = self.book_gongdaeUI.listWidget_book_B1_gongdae.currentRow()

        self.sender(self.client_socket, "gongdae")
        gongdae = self.receiver(self.client_socket)
        disable = self.getKeysByValue(gongdae[0], 1)
        if row in disable:
                QMessageBox.about(self, 'System', '예약 할 수 없는 자리입니다.')
                return

        location = "gongdae"
        book_floor = 'B1'
        book_num = row
        item = self.book_gongdaeUI.listWidget_book_B1_gongdae.currentItem()
        self.askUI.show()

    def click_book_gongdae_B2(self):
        global location, book_floor, book_num, item

        row = self.book_gongdaeUI.listWidget_book_B2_gongdae.currentRow()

        self.sender(self.client_socket, "gongdae")
        gongdae = self.receiver(self.client_socket)
        disable = self.getKeysByValue(gongdae[0], 1)
        if row in disable:
            QMessageBox.about(self, 'System', '예약 할 수 없는 자리입니다.')
            return

        location = "gongdae"
        book_floor = 'B2'
        book_num = row
        item = self.book_gongdaeUI.listWidget_book_B2_gongdae.currentItem()
        self.askUI.show()

    def click_book_gongdae_B3(self):
        global location, book_floor, book_num, item

        row = self.book_gongdaeUI.listWidget_book_B3_gongdae.currentRow()

        self.sender(self.client_socket, "gongdae")
        gongdae = self.receiver(self.client_socket)
        disable = self.getKeysByValue(gongdae[0], 1)
        if row in disable:
            QMessageBox.about(self, 'System', '예약 할 수 없는 자리입니다.')
            return

        location = "gongdae"
        book_floor = 'B3'
        book_num = row
        item = self.book_gongdaeUI.listWidget_book_B3_gongdae.currentItem()
        self.askUI.show()

    def click_book_sanhak_B1(self):
        global location, book_floor, book_num, item

        row = self.book_sanhakUI.listWidget_book_B1_sanhak.currentRow()

        self.sender(self.client_socket, "sanhak")
        sanhak = self.receiver(self.client_socket)
        disable = self.getKeysByValue(sanhak[0], 1)
        if row in disable:
                QMessageBox.about(self, 'System', '예약 할 수 없는 자리입니다.')
                return

        location = "sanhak"
        book_floor = 'B1'
        book_num = row
        item = self.book_sanhakUI.listWidget_book_B1_sanhak.currentItem()
        self.askUI.show()

    def click_book_sanhak_B2(self):
        global location, book_floor, book_num, item

        row = self.book_sanhakUI.listWidget_book_B2_sanhak.currentRow()

        self.sender(self.client_socket, "sanhak")
        sanhak = self.receiver(self.client_socket)
        disable = self.getKeysByValue(sanhak[0], 1)
        if row in disable:
            QMessageBox.about(self, 'System', '예약 할 수 없는 자리입니다.')
            return

        location = "sanhak"
        book_floor = 'B2'
        book_num = row
        item = self.book_sanhakUI.listWidget_book_B2_sanhak.currentItem()
        self.askUI.show()

    def click_book_sanhak_B3(self):
        global location, book_floor, book_num, item

        row = self.book_sanhakUI.listWidget_book_B3_sanhak.currentRow()

        self.sender(self.client_socket, "sanhak")
        sanhak = self.receiver(self.client_socket)
        disable = self.getKeysByValue(sanhak[0], 1)
        if row in disable:
            QMessageBox.about(self, 'System', '예약 할 수 없는 자리입니다.')
            return

        location = "sanhak"
        book_floor = 'B3'
        book_num = row
        item = self.book_sanhakUI.listWidget_book_B3_sanhak.currentItem()
        self.askUI.show()

    def click_book_sanhak_B4(self):
        global location, book_floor, book_num, item

        row = self.book_sanhakUI.listWidget_book_B4_sanhak.currentRow()

        self.sender(self.client_socket, "sanhak")
        sanhak = self.receiver(self.client_socket)
        disable = self.getKeysByValue(sanhak[0], 1)
        if row in disable:
            QMessageBox.about(self, 'System', '예약 할 수 없는 자리입니다.')
            return

        location = "sanhak"
        book_floor = 'B4'
        book_num = row
        item = self.book_sanhakUI.listWidget_book_B4_sanhak.currentItem()
        self.askUI.show()

    def click_book_haebong_B1(self):
        global location, book_floor, book_num, item

        row = self.book_haebongUI.listWidget_book_B1_haebong.currentRow()

        self.sender(self.client_socket, "haebong")
        haebong = self.receiver(self.client_socket)
        disable = self.getKeysByValue(haebong[0], 1)
        if row in disable:
                QMessageBox.about(self, 'System', '예약 할 수 없는 자리입니다.')
                return

        location = "haebong"
        book_floor = 'B1'
        book_num = row
        item = self.book_haebongUI.listWidget_book_B1_haebong.currentItem()
        self.askUI.show()

    def click_book_haebong_B2(self):
        global location, book_floor, book_num, item

        row = self.book_haebongUI.listWidget_book_B2_haebong.currentRow()

        self.sender(self.client_socket, "haebong")
        haebong = self.receiver(self.client_socket)
        disable = self.getKeysByValue(haebong[0], 1)
        if row in disable:
            QMessageBox.about(self, 'System', '예약 할 수 없는 자리입니다.')
            return

        location = "haebong"
        book_floor = 'B2'
        book_num = row
        item = self.book_haebongUI.listWidget_book_B2_haebong.currentItem()
        self.askUI.show()

    def click_book_back(self):
        self.bookUI.show()
        self.book_singongUI.close()
        self.book_gongdaeUI.close()
        self.book_sanhakUI.close()
        self.book_haebongUI.close()
        
    def click_book_singong(self):
        self.sender(self.client_socket, "singong")
        singong = self.receiver(self.client_socket)
        for i in range(0, 4):
            able = self.getKeysByValue(singong[i], 0)
            disable = self.getKeysByValue(singong[i], 1)
            if i == 0:  # B1층
                for key in able:
                    if key == 0:
                        self.book_singongUI.listWidget_book_B1_singong.item(0).setBackground(blue_brush)
                    elif key == 1:
                        self.book_singongUI.listWidget_book_B1_singong.item(1).setBackground(blue_brush)
                    elif key == 2:
                        self.book_singongUI.listWidget_book_B1_singong.item(2).setBackground(blue_brush)
                    elif key == 3:
                        self.book_singongUI.listWidget_book_B1_singong.item(3).setBackground(blue_brush)
                    elif key == 4:
                        self.book_singongUI.listWidget_book_B1_singong.item(4).setBackground(blue_brush)
                for key in disable:
                    if key == 0:
                        self.book_singongUI.listWidget_book_B1_singong.item(0).setBackground(red_brush)
                    elif key == 1:
                        self.book_singongUI.listWidget_book_B1_singong.item(1).setBackground(red_brush)
                    elif key == 2:
                        self.book_singongUI.listWidget_book_B1_singong.item(2).setBackground(red_brush)
                    elif key == 3:
                        self.book_singongUI.listWidget_book_B1_singong.item(3).setBackground(red_brush)
                    elif key == 4:
                        self.book_singongUI.listWidget_book_B1_singong.item(4).setBackground(red_brush)
            elif i == 1:  # B2층
                for key in able:
                    if key == 0:
                        self.book_singongUI.listWidget_book_B2_singong.item(0).setBackground(blue_brush)
                    elif key == 1:
                        self.book_singongUI.listWidget_book_B2_singong.item(1).setBackground(blue_brush)
                    elif key == 2:
                        self.book_singongUI.listWidget_book_B2_singong.item(2).setBackground(blue_brush)
                    elif key == 3:
                        self.book_singongUI.listWidget_book_B2_singong.item(3).setBackground(blue_brush)
                    elif key == 4:
                        self.book_singongUI.listWidget_book_B2_singong.item(4).setBackground(blue_brush)
                for key in disable:
                    if key == 0:
                        self.book_singongUI.listWidget_book_B2_singong.item(0).setBackground(red_brush)
                    elif key == 1:
                        self.book_singongUI.listWidget_book_B2_singong.item(1).setBackground(red_brush)
                    elif key == 2:
                        self.book_singongUI.listWidget_book_B2_singong.item(2).setBackground(red_brush)
                    elif key == 3:
                        self.book_singongUI.listWidget_book_B2_singong.item(3).setBackground(red_brush)
                    elif key == 4:
                        self.book_singongUI.listWidget_book_B2_singong.item(4).setBackground(red_brush)
            elif i == 2:  # B3층
                for key in able:
                    if key == 0:
                        self.book_singongUI.listWidget_book_B3_singong.item(0).setBackground(blue_brush)
                    elif key == 1:
                        self.book_singongUI.listWidget_book_B3_singong.item(1).setBackground(blue_brush)
                    elif key == 2:
                        self.book_singongUI.listWidget_book_B3_singong.item(2).setBackground(blue_brush)
                    elif key == 3:
                        self.book_singongUI.listWidget_book_B3_singong.item(3).setBackground(blue_brush)
                    elif key == 4:
                        self.book_singongUI.listWidget_book_B3_singong.item(4).setBackground(blue_brush)
                for key in disable:
                    if key == 0:
                        self.book_singongUI.listWidget_book_B3_singong.item(0).setBackground(red_brush)
                    elif key == 1:
                        self.book_singongUI.listWidget_book_B3_singong.item(1).setBackground(red_brush)
                    elif key == 2:
                        self.book_singongUI.listWidget_book_B3_singong.item(2).setBackground(red_brush)
                    elif key == 3:
                        self.book_singongUI.listWidget_book_B3_singong.item(3).setBackground(red_brush)
                    elif key == 4:
                        self.book_singongUI.listWidget_book_B3_singong.item(4).setBackground(red_brush)
            elif i == 3:  # B4층
                for key in able:
                    if key == 0:
                        self.book_singongUI.listWidget_book_B4_singong.item(0).setBackground(blue_brush)
                    elif key == 1:
                        self.book_singongUI.listWidget_book_B4_singong.item(1).setBackground(blue_brush)
                    elif key == 2:
                        self.book_singongUI.listWidget_book_B4_singong.item(2).setBackground(blue_brush)
                    elif key == 3:
                        self.book_singongUI.listWidget_book_B4_singong.item(3).setBackground(blue_brush)
                    elif key == 4:
                        self.book_singongUI.listWidget_book_B4_singong.item(4).setBackground(blue_brush)
                for key in disable:
                    if key == 0:
                        self.book_singongUI.listWidget_book_B4_singong.item(0).setBackground(red_brush)
                    elif key == 1:
                        self.book_singongUI.listWidget_book_B4_singong.item(1).setBackground(red_brush)
                    elif key == 2:
                        self.book_singongUI.listWidget_book_B4_singong.item(2).setBackground(red_brush)
                    elif key == 3:
                        self.book_singongUI.listWidget_book_B4_singong.item(3).setBackground(red_brush)
                    elif key == 4:
                        self.book_singongUI.listWidget_book_B4_singong.item(4).setBackground(red_brush)
        self.book_singongUI.show()
        self.bookUI.close()

    def click_book_gongdae(self):
        self.sender(self.client_socket, "gongdae")
        gongdae = self.receiver(self.client_socket)
        for i in range(0, 3):
            able = self.getKeysByValue(gongdae[i], 0)
            disable = self.getKeysByValue(gongdae[i], 1)
            if i == 0:  # B1층
                for key in able:
                    if key == 0:
                        self.book_gongdaeUI.listWidget_book_B1_gongdae.item(0).setBackground(blue_brush)
                    elif key == 1:
                        self.book_gongdaeUI.listWidget_book_B1_gongdae.item(1).setBackground(blue_brush)
                    elif key == 2:
                        self.book_gongdaeUI.listWidget_book_B1_gongdae.item(2).setBackground(blue_brush)
                    elif key == 3:
                        self.book_gongdaeUI.listWidget_book_B1_gongdae.item(3).setBackground(blue_brush)
                    elif key == 4:
                        self.book_gongdaeUI.listWidget_book_B1_gongdae.item(4).setBackground(blue_brush)
                for key in disable:
                    if key == 0:
                        self.book_gongdaeUI.listWidget_book_B1_gongdae.item(0).setBackground(red_brush)
                    elif key == 1:
                        self.book_gongdaeUI.listWidget_book_B1_gongdae.item(1).setBackground(red_brush)
                    elif key == 2:
                        self.book_gongdaeUI.listWidget_book_B1_gongdae.item(2).setBackground(red_brush)
                    elif key == 3:
                        self.book_gongdaeUI.listWidget_book_B1_gongdae.item(3).setBackground(red_brush)
                    elif key == 4:
                        self.book_gongdaeUI.listWidget_book_B1_gongdae.item(4).setBackground(red_brush)
            elif i == 1:  # B2층
                for key in able:
                    if key == 0:
                        self.book_gongdaeUI.listWidget_book_B2_gongdae.item(0).setBackground(blue_brush)
                    elif key == 1:
                        self.book_gongdaeUI.listWidget_book_B2_gongdae.item(1).setBackground(blue_brush)
                    elif key == 2:
                        self.book_gongdaeUI.listWidget_book_B2_gongdae.item(2).setBackground(blue_brush)
                    elif key == 3:
                        self.book_gongdaeUI.listWidget_book_B2_gongdae.item(3).setBackground(blue_brush)
                    elif key == 4:
                        self.book_gongdaeUI.listWidget_book_B2_gongdae.item(4).setBackground(blue_brush)
                for key in disable:
                    if key == 0:
                        self.book_gongdaeUI.listWidget_book_B2_gongdae.item(0).setBackground(red_brush)
                    elif key == 1:
                        self.book_gongdaeUI.listWidget_book_B2_gongdae.item(1).setBackground(red_brush)
                    elif key == 2:
                        self.book_gongdaeUI.listWidget_book_B2_gongdae.item(2).setBackground(red_brush)
                    elif key == 3:
                        self.book_gongdaeUI.listWidget_book_B2_gongdae.item(3).setBackground(red_brush)
                    elif key == 4:
                        self.book_gongdaeUI.listWidget_book_B2_gongdae.item(4).setBackground(red_brush)
            elif i == 2:  # B3층
                for key in able:
                    if key == 0:
                        self.book_gongdaeUI.listWidget_book_B3_gongdae.item(0).setBackground(blue_brush)
                    elif key == 1:
                        self.book_gongdaeUI.listWidget_book_B3_gongdae.item(1).setBackground(blue_brush)
                    elif key == 2:
                        self.book_gongdaeUI.listWidget_book_B3_gongdae.item(2).setBackground(blue_brush)
                    elif key == 3:
                        self.book_gongdaeUI.listWidget_book_B3_gongdae.item(3).setBackground(blue_brush)
                    elif key == 4:
                        self.book_gongdaeUI.listWidget_book_B3_gongdae.item(4).setBackground(blue_brush)
                for key in disable:
                    if key == 0:
                        self.book_gongdaeUI.listWidget_book_B3_gongdae.item(0).setBackground(red_brush)
                    elif key == 1:
                        self.book_gongdaeUI.listWidget_book_B3_gongdae.item(1).setBackground(red_brush)
                    elif key == 2:
                        self.book_gongdaeUI.listWidget_book_B3_gongdae.item(2).setBackground(red_brush)
                    elif key == 3:
                        self.book_gongdaeUI.listWidget_book_B3_gongdae.item(3).setBackground(red_brush)
                    elif key == 4:
                        self.book_gongdaeUI.listWidget_book_B3_gongdae.item(4).setBackground(red_brush)
        self.book_gongdaeUI.show()
        self.bookUI.close()

    def click_book_sanhak(self):
        self.sender(self.client_socket, "sanhak")
        sanhak = self.receiver(self.client_socket)
        for i in range(0, 4):
            able = self.getKeysByValue(sanhak[i], 0)
            disable = self.getKeysByValue(sanhak[i], 1)
            if i == 0:  # B1층
                for key in able:
                    if key == 0:
                        self.book_sanhakUI.listWidget_book_B1_sanhak.item(0).setBackground(blue_brush)
                    elif key == 1:
                        self.book_sanhakUI.listWidget_book_B1_sanhak.item(1).setBackground(blue_brush)
                    elif key == 2:
                        self.book_sanhakUI.listWidget_book_B1_sanhak.item(2).setBackground(blue_brush)
                    elif key == 3:
                        self.book_sanhakUI.listWidget_book_B1_sanhak.item(3).setBackground(blue_brush)
                    elif key == 4:
                        self.book_sanhakUI.listWidget_book_B1_sanhak.item(4).setBackground(blue_brush)
                for key in disable:
                    if key == 0:
                        self.book_sanhakUI.listWidget_book_B1_sanhak.item(0).setBackground(red_brush)
                    elif key == 1:
                        self.book_sanhakUI.listWidget_book_B1_sanhak.item(1).setBackground(red_brush)
                    elif key == 2:
                        self.book_sanhakUI.listWidget_book_B1_sanhak.item(2).setBackground(red_brush)
                    elif key == 3:
                        self.book_sanhakUI.listWidget_book_B1_sanhak.item(3).setBackground(red_brush)
                    elif key == 4:
                        self.book_sanhakUI.listWidget_book_B1_sanhak.item(4).setBackground(red_brush)
            elif i == 1:  # B2층
                for key in able:
                    if key == 0:
                        self.book_sanhakUI.listWidget_book_B2_sanhak.item(0).setBackground(blue_brush)
                    elif key == 1:
                        self.book_sanhakUI.listWidget_book_B2_sanhak.item(1).setBackground(blue_brush)
                    elif key == 2:
                        self.book_sanhakUI.listWidget_book_B2_sanhak.item(2).setBackground(blue_brush)
                    elif key == 3:
                        self.book_sanhakUI.listWidget_book_B2_sanhak.item(3).setBackground(blue_brush)
                    elif key == 4:
                        self.book_sanhakUI.listWidget_book_B2_sanhak.item(4).setBackground(blue_brush)
                for key in disable:
                    if key == 0:
                        self.book_sanhakUI.listWidget_book_B2_sanhak.item(0).setBackground(red_brush)
                    elif key == 1:
                        self.book_sanhakUI.listWidget_book_B2_sanhak.item(1).setBackground(red_brush)
                    elif key == 2:
                        self.book_sanhakUI.listWidget_book_B2_sanhak.item(2).setBackground(red_brush)
                    elif key == 3:
                        self.book_sanhakUI.listWidget_book_B2_sanhak.item(3).setBackground(red_brush)
                    elif key == 4:
                        self.book_sanhakUI.listWidget_book_B2_sanhak.item(4).setBackground(red_brush)
            elif i == 2:  # B3층
                for key in able:
                    if key == 0:
                        self.book_sanhakUI.listWidget_book_B3_sanhak.item(0).setBackground(blue_brush)
                    elif key == 1:
                        self.book_sanhakUI.listWidget_book_B3_sanhak.item(1).setBackground(blue_brush)
                    elif key == 2:
                        self.book_sanhakUI.listWidget_book_B3_sanhak.item(2).setBackground(blue_brush)
                    elif key == 3:
                        self.book_sanhakUI.listWidget_book_B3_sanhak.item(3).setBackground(blue_brush)
                    elif key == 4:
                        self.book_sanhakUI.listWidget_book_B3_sanhak.item(4).setBackground(blue_brush)
                for key in disable:
                    if key == 0:
                        self.book_sanhakUI.listWidget_book_B3_sanhak.item(0).setBackground(red_brush)
                    elif key == 1:
                        self.book_sanhakUI.listWidget_book_B3_sanhak.item(1).setBackground(red_brush)
                    elif key == 2:
                        self.book_sanhakUI.listWidget_book_B3_sanhak.item(2).setBackground(red_brush)
                    elif key == 3:
                        self.book_sanhakUI.listWidget_book_B3_sanhak.item(3).setBackground(red_brush)
                    elif key == 4:
                        self.book_sanhakUI.listWidget_book_B3_sanhak.item(4).setBackground(red_brush)
            elif i == 3:  # B4층
                for key in able:
                    if key == 0:
                        self.book_sanhakUI.listWidget_book_B4_sanhak.item(0).setBackground(blue_brush)
                    elif key == 1:
                        self.book_sanhakUI.listWidget_book_B4_sanhak.item(1).setBackground(blue_brush)
                    elif key == 2:
                        self.book_sanhakUI.listWidget_book_B4_sanhak.item(2).setBackground(blue_brush)
                    elif key == 3:
                        self.book_sanhakUI.listWidget_book_B4_sanhak.item(3).setBackground(blue_brush)
                    elif key == 4:
                        self.book_sanhakUI.listWidget_book_B4_sanhak.item(4).setBackground(blue_brush)
                for key in disable:
                    if key == 0:
                        self.book_sanhakUI.listWidget_book_B4_sanhak.item(0).setBackground(red_brush)
                    elif key == 1:
                        self.book_sanhakUI.listWidget_book_B4_sanhak.item(1).setBackground(red_brush)
                    elif key == 2:
                        self.book_sanhakUI.listWidget_book_B4_sanhak.item(2).setBackground(red_brush)
                    elif key == 3:
                        self.book_sanhakUI.listWidget_book_B4_sanhak.item(3).setBackground(red_brush)
                    elif key == 4:
                        self.book_sanhakUI.listWidget_book_B4_sanhak.item(4).setBackground(red_brush)
        self.book_sanhakUI.show()
        self.bookUI.close()

    def click_book_haebong(self):
        self.sender(self.client_socket, "haebong")
        haebong = self.receiver(self.client_socket)
        for i in range(0, 2):
            able = self.getKeysByValue(haebong[i], 0)
            disable = self.getKeysByValue(haebong[i], 1)
            if i == 0:  # B1층
                for key in able:
                    if key == 0:
                        self.book_haebongUI.listWidget_book_B1_haebong.item(0).setBackground(blue_brush)
                    elif key == 1:
                        self.book_haebongUI.listWidget_book_B1_haebong.item(1).setBackground(blue_brush)
                    elif key == 2:
                        self.book_haebongUI.listWidget_book_B1_haebong.item(2).setBackground(blue_brush)
                    elif key == 3:
                        self.book_haebongUI.listWidget_book_B1_haebong.item(3).setBackground(blue_brush)
                    elif key == 4:
                        self.book_haebongUI.listWidget_book_B1_haebong.item(4).setBackground(blue_brush)
                for key in disable:
                    if key == 0:
                        self.book_haebongUI.listWidget_book_B1_haebong.item(0).setBackground(red_brush)
                    elif key == 1:
                        self.book_haebongUI.listWidget_book_B1_haebong.item(1).setBackground(red_brush)
                    elif key == 2:
                        self.book_haebongUI.listWidget_book_B1_haebong.item(2).setBackground(red_brush)
                    elif key == 3:
                        self.book_haebongUI.listWidget_book_B1_haebong.item(3).setBackground(red_brush)
                    elif key == 4:
                        self.book_haebongUI.listWidget_book_B1_haebong.item(4).setBackground(red_brush)
            elif i == 1:  # B2층
                for key in able:
                    if key == 0:
                        self.book_haebongUI.listWidget_book_B2_haebong.item(0).setBackground(blue_brush)
                    elif key == 1:
                        self.book_haebongUI.listWidget_book_B2_haebong.item(1).setBackground(blue_brush)
                    elif key == 2:
                        self.book_haebongUI.listWidget_book_B2_haebong.item(2).setBackground(blue_brush)
                    elif key == 3:
                        self.book_haebongUI.listWidget_book_B2_haebong.item(3).setBackground(blue_brush)
                    elif key == 4:
                        self.book_haebongUI.listWidget_book_B2_haebong.item(4).setBackground(blue_brush)
                for key in disable:
                    if key == 0:
                        self.book_haebongUI.listWidget_book_B2_haebong.item(0).setBackground(red_brush)
                    elif key == 1:
                        self.book_haebongUI.listWidget_book_B2_haebong.item(1).setBackground(red_brush)
                    elif key == 2:
                        self.book_haebongUI.listWidget_book_B2_haebong.item(2).setBackground(red_brush)
                    elif key == 3:
                        self.book_haebongUI.listWidget_book_B2_haebong.item(3).setBackground(red_brush)
                    elif key == 4:
                        self.book_haebongUI.listWidget_book_B2_haebong.item(4).setBackground(red_brush)
        self.book_haebongUI.show()
        self.bookUI.close()

    def click_check_back(self):
        self.checkUI.show()
        self.check_singongUI.close()
        self.check_gongdaeUI.close()
        self.check_sanhakUI.close()
        self.check_haebongUI.close()

    def click_check_singong(self):
        self.sender(self.client_socket, "singong")
        singong = self.receiver(self.client_socket)
        for i in range(0, 4):
            able = self.getKeysByValue(singong[i], 0)
            disable = self.getKeysByValue(singong[i], 1)
            if i == 0: # B1층
                for key in able:
                    if key == 0:
                        self.check_singongUI.listWidget_show_B1_singong.item(0).setBackground(blue_brush)
                    elif key == 1:
                        self.check_singongUI.listWidget_show_B1_singong.item(1).setBackground(blue_brush)
                    elif key == 2:
                        self.check_singongUI.listWidget_show_B1_singong.item(2).setBackground(blue_brush)
                    elif key == 3:
                        self.check_singongUI.listWidget_show_B1_singong.item(3).setBackground(blue_brush)
                    elif key == 4:
                        self.check_singongUI.listWidget_show_B1_singong.item(4).setBackground(blue_brush)
                for key in disable:
                    if key == 0:
                        self.check_singongUI.listWidget_show_B1_singong.item(0).setBackground(red_brush)
                    elif key == 1:
                        self.check_singongUI.listWidget_show_B1_singong.item(1).setBackground(red_brush)
                    elif key == 2:
                        self.check_singongUI.listWidget_show_B1_singong.item(2).setBackground(red_brush)
                    elif key == 3:
                        self.check_singongUI.listWidget_show_B1_singong.item(3).setBackground(red_brush)
                    elif key == 4:
                        self.check_singongUI.listWidget_show_B1_singong.item(4).setBackground(red_brush)
            elif i == 1:  # B2층
                for key in able:
                    if key == 0:
                        self.check_singongUI.listWidget_show_B2_singong.item(0).setBackground(blue_brush)
                    elif key == 1:
                        self.check_singongUI.listWidget_show_B2_singong.item(1).setBackground(blue_brush)
                    elif key == 2:
                        self.check_singongUI.listWidget_show_B2_singong.item(2).setBackground(blue_brush)
                    elif key == 3:
                        self.check_singongUI.listWidget_show_B2_singong.item(3).setBackground(blue_brush)
                    elif key == 4:
                        self.check_singongUI.listWidget_show_B2_singong.item(4).setBackground(blue_brush)
                for key in disable:
                    if key == 0:
                        self.check_singongUI.listWidget_show_B2_singong.item(0).setBackground(red_brush)
                    elif key == 1:
                        self.check_singongUI.listWidget_show_B2_singong.item(1).setBackground(red_brush)
                    elif key == 2:
                        self.check_singongUI.listWidget_show_B2_singong.item(2).setBackground(red_brush)
                    elif key == 3:
                        self.check_singongUI.listWidget_show_B2_singong.item(3).setBackground(red_brush)
                    elif key == 4:
                        self.check_singongUI.listWidget_show_B2_singong.item(4).setBackground(red_brush)
            elif i == 2:  # B3층
                for key in able:
                    if key == 0:
                        self.check_singongUI.listWidget_show_B3_singong.item(0).setBackground(blue_brush)
                    elif key == 1:
                        self.check_singongUI.listWidget_show_B3_singong.item(1).setBackground(blue_brush)
                    elif key == 2:
                        self.check_singongUI.listWidget_show_B3_singong.item(2).setBackground(blue_brush)
                    elif key == 3:
                        self.check_singongUI.listWidget_show_B3_singong.item(3).setBackground(blue_brush)
                    elif key == 4:
                        self.check_singongUI.listWidget_show_B3_singong.item(4).setBackground(blue_brush)
                for key in disable:
                    if key == 0:
                        self.check_singongUI.listWidget_show_B3_singong.item(0).setBackground(red_brush)
                    elif key == 1:
                        self.check_singongUI.listWidget_show_B3_singong.item(1).setBackground(red_brush)
                    elif key == 2:
                        self.check_singongUI.listWidget_show_B3_singong.item(2).setBackground(red_brush)
                    elif key == 3:
                        self.check_singongUI.listWidget_show_B3_singong.item(3).setBackground(red_brush)
                    elif key == 4:
                        self.check_singongUI.listWidget_show_B3_singong.item(4).setBackground(red_brush)
            elif i == 3:  # B4층
                for key in able:
                    if key == 0:
                        self.check_singongUI.listWidget_show_B4_singong.item(0).setBackground(blue_brush)
                    elif key == 1:
                        self.check_singongUI.listWidget_show_B4_singong.item(1).setBackground(blue_brush)
                    elif key == 2:
                        self.check_singongUI.listWidget_show_B4_singong.item(2).setBackground(blue_brush)
                    elif key == 3:
                        self.check_singongUI.listWidget_show_B4_singong.item(3).setBackground(blue_brush)
                    elif key == 4:
                        self.check_singongUI.listWidget_show_B4_singong.item(4).setBackground(blue_brush)
                for key in disable:
                    if key == 0:
                        self.check_singongUI.listWidget_show_B4_singong.item(0).setBackground(red_brush)
                    elif key == 1:
                        self.check_singongUI.listWidget_show_B4_singong.item(1).setBackground(red_brush)
                    elif key == 2:
                        self.check_singongUI.listWidget_show_B4_singong.item(2).setBackground(red_brush)
                    elif key == 3:
                        self.check_singongUI.listWidget_show_B4_singong.item(3).setBackground(red_brush)
                    elif key == 4:
                        self.check_singongUI.listWidget_show_B4_singong.item(4).setBackground(red_brush)
        self.check_singongUI.show()
        self.checkUI.close()

    def click_check_gongdae(self):
        self.sender(self.client_socket, "gongdae")
        gongdae = self.receiver(self.client_socket)
        for i in range(0, 3):
            able = self.getKeysByValue(gongdae[i], 0)
            disable = self.getKeysByValue(gongdae[i], 1)
            if i == 0:  # B1층
                for key in able:
                    if key == 0:
                        self.check_gongdaeUI.listWidget_show_B1_gongdae.item(0).setBackground(blue_brush)
                    elif key == 1:
                        self.check_gongdaeUI.listWidget_show_B1_gongdae.item(1).setBackground(blue_brush)
                    elif key == 2:
                        self.check_gongdaeUI.listWidget_show_B1_gongdae.item(2).setBackground(blue_brush)
                    elif key == 3:
                        self.check_gongdaeUI.listWidget_show_B1_gongdae.item(3).setBackground(blue_brush)
                    elif key == 4:
                        self.check_gongdaeUI.listWidget_show_B1_gongdae.item(4).setBackground(blue_brush)
                for key in disable:
                    if key == 0:
                        self.check_gongdaeUI.listWidget_show_B1_gongdae.item(0).setBackground(red_brush)
                    elif key == 1:
                        self.check_gongdaeUI.listWidget_show_B1_gongdae.item(1).setBackground(red_brush)
                    elif key == 2:
                        self.check_gongdaeUI.listWidget_show_B1_gongdae.item(2).setBackground(red_brush)
                    elif key == 3:
                        self.check_gongdaeUI.listWidget_show_B1_gongdae.item(3).setBackground(red_brush)
                    elif key == 4:
                        self.check_gongdaeUI.listWidget_show_B1_gongdae.item(4).setBackground(red_brush)
            elif i == 1:  # B2층
                for key in able:
                    if key == 0:
                        self.check_gongdaeUI.listWidget_show_B2_gongdae.item(0).setBackground(blue_brush)
                    elif key == 1:
                        self.check_gongdaeUI.listWidget_show_B2_gongdae.item(1).setBackground(blue_brush)
                    elif key == 2:
                        self.check_gongdaeUI.listWidget_show_B2_gongdae.item(2).setBackground(blue_brush)
                    elif key == 3:
                        self.check_gongdaeUI.listWidget_show_B2_gongdae.item(3).setBackground(blue_brush)
                    elif key == 4:
                        self.check_gongdaeUI.listWidget_show_B2_gongdae.item(4).setBackground(blue_brush)
                for key in disable:
                    if key == 0:
                        self.check_gongdaeUI.listWidget_show_B2_gongdae.item(0).setBackground(red_brush)
                    elif key == 1:
                        self.check_gongdaeUI.listWidget_show_B2_gongdae.item(1).setBackground(red_brush)
                    elif key == 2:
                        self.check_gongdaeUI.listWidget_show_B2_gongdae.item(2).setBackground(red_brush)
                    elif key == 3:
                        self.check_gongdaeUI.listWidget_show_B2_gongdae.item(3).setBackground(red_brush)
                    elif key == 4:
                        self.check_gongdaeUI.listWidget_show_B2_gongdae.item(4).setBackground(red_brush)
            elif i == 2:  # B3층
                for key in able:
                    if key == 0:
                        self.check_gongdaeUI.listWidget_show_B3_gongdae.item(0).setBackground(blue_brush)
                    elif key == 1:
                        self.check_gongdaeUI.listWidget_show_B3_gongdae.item(1).setBackground(blue_brush)
                    elif key == 2:
                        self.check_gongdaeUI.listWidget_show_B3_gongdae.item(2).setBackground(blue_brush)
                    elif key == 3:
                        self.check_gongdaeUI.listWidget_show_B3_gongdae.item(3).setBackground(blue_brush)
                    elif key == 4:
                        self.check_gongdaeUI.listWidget_show_B3_gongdae.item(4).setBackground(blue_brush)
                for key in disable:
                    if key == 0:
                        self.check_gongdaeUI.listWidget_show_B3_gongdae.item(0).setBackground(red_brush)
                    elif key == 1:
                        self.check_gongdaeUI.listWidget_show_B3_gongdae.item(1).setBackground(red_brush)
                    elif key == 2:
                        self.check_gongdaeUI.listWidget_show_B3_gongdae.item(2).setBackground(red_brush)
                    elif key == 3:
                        self.check_gongdaeUI.listWidget_show_B3_gongdae.item(3).setBackground(red_brush)
                    elif key == 4:
                        self.check_gongdaeUI.listWidget_show_B3_gongdae.item(4).setBackground(red_brush)
        self.check_gongdaeUI.show()
        self.checkUI.close()

    def click_check_sanhak(self):
        self.sender(self.client_socket, "sanhak")
        sanhak = self.receiver(self.client_socket)
        for i in range(0, 4):
            able = self.getKeysByValue(sanhak[i], 0)
            disable = self.getKeysByValue(sanhak[i], 1)
            if i == 0:  # B1층
                for key in able:
                    if key == 0:
                        self.check_sanhakUI.listWidget_show_B1_sanhak.item(0).setBackground(blue_brush)
                    elif key == 1:
                        self.check_sanhakUI.listWidget_show_B1_sanhak.item(1).setBackground(blue_brush)
                    elif key == 2:
                        self.check_sanhakUI.listWidget_show_B1_sanhak.item(2).setBackground(blue_brush)
                    elif key == 3:
                        self.check_sanhakUI.listWidget_show_B1_sanhak.item(3).setBackground(blue_brush)
                    elif key == 4:
                        self.check_sanhakUI.listWidget_show_B1_sanhak.item(4).setBackground(blue_brush)
                for key in disable:
                    if key == 0:
                        self.check_sanhakUI.listWidget_show_B1_sanhak.item(0).setBackground(red_brush)
                    elif key == 1:
                        self.check_sanhakUI.listWidget_show_B1_sanhak.item(1).setBackground(red_brush)
                    elif key == 2:
                        self.check_sanhakUI.listWidget_show_B1_sanhak.item(2).setBackground(red_brush)
                    elif key == 3:
                        self.check_sanhakUI.listWidget_show_B1_sanhak.item(3).setBackground(red_brush)
                    elif key == 4:
                        self.check_sanhakUI.listWidget_show_B1_sanhak.item(4).setBackground(red_brush)
            elif i == 1:  # B2층
                for key in able:
                    if key == 0:
                        self.check_sanhakUI.listWidget_show_B2_sanhak.item(0).setBackground(blue_brush)
                    elif key == 1:
                        self.check_sanhakUI.listWidget_show_B2_sanhak.item(1).setBackground(blue_brush)
                    elif key == 2:
                        self.check_sanhakUI.listWidget_show_B2_sanhak.item(2).setBackground(blue_brush)
                    elif key == 3:
                        self.check_sanhakUI.listWidget_show_B2_sanhak.item(3).setBackground(blue_brush)
                    elif key == 4:
                        self.check_sanhakUI.listWidget_show_B2_sanhak.item(4).setBackground(blue_brush)
                for key in disable:
                    if key == 0:
                        self.check_sanhakUI.listWidget_show_B2_sanhak.item(0).setBackground(red_brush)
                    elif key == 1:
                        self.check_sanhakUI.listWidget_show_B2_sanhak.item(1).setBackground(red_brush)
                    elif key == 2:
                        self.check_sanhakUI.listWidget_show_B2_sanhak.item(2).setBackground(red_brush)
                    elif key == 3:
                        self.check_sanhakUI.listWidget_show_B2_sanhak.item(3).setBackground(red_brush)
                    elif key == 4:
                        self.check_sanhakUI.listWidget_show_B2_sanhak.item(4).setBackground(red_brush)
            elif i == 2:  # B3층
                for key in able:
                    if key == 0:
                        self.check_sanhakUI.listWidget_show_B3_sanhak.item(0).setBackground(blue_brush)
                    elif key == 1:
                        self.check_sanhakUI.listWidget_show_B3_sanhak.item(1).setBackground(blue_brush)
                    elif key == 2:
                        self.check_sanhakUI.listWidget_show_B3_sanhak.item(2).setBackground(blue_brush)
                    elif key == 3:
                        self.check_sanhakUI.listWidget_show_B3_sanhak.item(3).setBackground(blue_brush)
                    elif key == 4:
                        self.check_sanhakUI.listWidget_show_B3_sanhak.item(4).setBackground(blue_brush)
                for key in disable:
                    if key == 0:
                        self.check_sanhakUI.listWidget_show_B3_sanhak.item(0).setBackground(red_brush)
                    elif key == 1:
                        self.check_sanhakUI.listWidget_show_B3_sanhak.item(1).setBackground(red_brush)
                    elif key == 2:
                        self.check_sanhakUI.listWidget_show_B3_sanhak.item(2).setBackground(red_brush)
                    elif key == 3:
                        self.check_sanhakUI.listWidget_show_B3_sanhak.item(3).setBackground(red_brush)
                    elif key == 4:
                        self.check_sanhakUI.listWidget_show_B3_sanhak.item(4).setBackground(red_brush)
            elif i == 3:  # B4층
                for key in able:
                    if key == 0:
                        self.check_sanhakUI.listWidget_show_B4_sanhak.item(0).setBackground(blue_brush)
                    elif key == 1:
                        self.check_sanhakUI.listWidget_show_B4_sanhak.item(1).setBackground(blue_brush)
                    elif key == 2:
                        self.check_sanhakUI.listWidget_show_B4_sanhak.item(2).setBackground(blue_brush)
                    elif key == 3:
                        self.check_sanhakUI.listWidget_show_B4_sanhak.item(3).setBackground(blue_brush)
                    elif key == 4:
                        self.check_sanhakUI.listWidget_show_B4_sanhak.item(4).setBackground(blue_brush)
                for key in disable:
                    if key == 0:
                        self.check_sanhakUI.listWidget_show_B4_sanhak.item(0).setBackground(red_brush)
                    elif key == 1:
                        self.check_sanhakUI.listWidget_show_B4_sanhak.item(1).setBackground(red_brush)
                    elif key == 2:
                        self.check_sanhakUI.listWidget_show_B4_sanhak.item(2).setBackground(red_brush)
                    elif key == 3:
                        self.check_sanhakUI.listWidget_show_B4_sanhak.item(3).setBackground(red_brush)
                    elif key == 4:
                        self.check_sanhakUI.listWidget_show_B4_sanhak.item(4).setBackground(red_brush)
        self.check_sanhakUI.show()
        self.checkUI.close()

    def click_check_haebong(self):
        self.sender(self.client_socket, "haebong")
        haebong = self.receiver(self.client_socket)
        for i in range(0, 2):
            able = self.getKeysByValue(haebong[i], 0)
            disable = self.getKeysByValue(haebong[i], 1)
            if i == 0:  # B1층
                for key in able:
                    if key == 0:
                        self.check_haebongUI.listWidget_show_B1_haebong.item(0).setBackground(blue_brush)
                    elif key == 1:
                        self.check_haebongUI.listWidget_show_B1_haebong.item(1).setBackground(blue_brush)
                    elif key == 2:
                        self.check_haebongUI.listWidget_show_B1_haebong.item(2).setBackground(blue_brush)
                    elif key == 3:
                        self.check_haebongUI.listWidget_show_B1_haebong.item(3).setBackground(blue_brush)
                    elif key == 4:
                        self.check_haebongUI.listWidget_show_B1_haebong.item(4).setBackground(blue_brush)
                for key in disable:
                    if key == 0:
                        self.check_haebongUI.listWidget_show_B1_haebong.item(0).setBackground(red_brush)
                    elif key == 1:
                        self.check_haebongUI.listWidget_show_B1_haebong.item(1).setBackground(red_brush)
                    elif key == 2:
                        self.check_haebongUI.listWidget_show_B1_haebong.item(2).setBackground(red_brush)
                    elif key == 3:
                        self.check_haebongUI.listWidget_show_B1_haebong.item(3).setBackground(red_brush)
                    elif key == 4:
                        self.check_haebongUI.listWidget_show_B1_haebong.item(4).setBackground(red_brush)
            elif i == 1:  # B2층
                for key in able:
                    if key == 0:
                        self.check_haebongUI.listWidget_show_B2_haebong.item(0).setBackground(blue_brush)
                    elif key == 1:
                        self.check_haebongUI.listWidget_show_B2_haebong.item(1).setBackground(blue_brush)
                    elif key == 2:
                        self.check_haebongUI.listWidget_show_B2_haebong.item(2).setBackground(blue_brush)
                    elif key == 3:
                        self.check_haebongUI.listWidget_show_B2_haebong.item(3).setBackground(blue_brush)
                    elif key == 4:
                        self.check_haebongUI.listWidget_show_B2_haebong.item(4).setBackground(blue_brush)
                for key in disable:
                    if key == 0:
                        self.check_haebongUI.listWidget_show_B2_haebong.item(0).setBackground(red_brush)
                    elif key == 1:
                        self.check_haebongUI.listWidget_show_B2_haebong.item(1).setBackground(red_brush)
                    elif key == 2:
                        self.check_haebongUI.listWidget_show_B2_haebong.item(2).setBackground(red_brush)
                    elif key == 3:
                        self.check_haebongUI.listWidget_show_B2_haebong.item(3).setBackground(red_brush)
                    elif key == 4:
                        self.check_haebongUI.listWidget_show_B2_haebong.item(4).setBackground(red_brush)
        self.check_haebongUI.show()
        self.checkUI.close()

    def click_back(self):
        self.mainUI.show()
        self.checkUI.close()
        self.bookUI.close()

    def click_check(self):
        self.checkUI.show()
        self.mainUI.close()

    def click_book(self):
        self.bookUI.show()
        self.mainUI.close()

    def getKeysByValue(self, dictOfElements, valueToFind):
        listOfKeys = list()
        listOfItems = dictOfElements.items()
        for item in listOfItems:
            if item[1] == valueToFind:
                listOfKeys.append(item[0])
        return listOfKeys

    def sender(self, client_socket, value):
        data = pickle.dumps(value)
        client_socket.send(data)

    def receiver(self, client_socket):
        data = client_socket.recv(1024)
        recv_data = pickle.loads(data)
        return recv_data

    def setting(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        IP = '192.168.57.1'
        PORT = 8888

        client_socket.connect((IP, PORT))
        print(self.receiver(client_socket))
        self.sender(client_socket, my_id)
        return client_socket


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
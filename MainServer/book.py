# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'book.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class bookUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(bookUI, self).__init__(parent)
        self.setupUi()
    def setupUi(self):
        # disable (but not hide) close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        self.setObjectName("Form")
        self.resize(574, 460)
        self.pushButton_book_singong = QtWidgets.QPushButton(self)
        self.pushButton_book_singong.setGeometry(QtCore.QRect(30, 40, 211, 161))
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(14)
        self.pushButton_book_singong.setFont(font)
        self.pushButton_book_singong.setObjectName("pushButton_book_singong")
        self.pushButton_book_haebong = QtWidgets.QPushButton(self)
        self.pushButton_book_haebong.setGeometry(QtCore.QRect(330, 250, 211, 161))
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(14)
        self.pushButton_book_haebong.setFont(font)
        self.pushButton_book_haebong.setObjectName("pushButton_book_haebong")
        self.pushButton_book_sanhak = QtWidgets.QPushButton(self)
        self.pushButton_book_sanhak.setGeometry(QtCore.QRect(30, 250, 211, 161))
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(14)
        self.pushButton_book_sanhak.setFont(font)
        self.pushButton_book_sanhak.setObjectName("pushButton_book_sanhak")
        self.pushButton_book_gongdae = QtWidgets.QPushButton(self)
        self.pushButton_book_gongdae.setGeometry(QtCore.QRect(330, 40, 211, 161))
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(14)
        self.pushButton_book_gongdae.setFont(font)
        self.pushButton_book_gongdae.setObjectName("pushButton_book_gongdae")
        self.label_book = QtWidgets.QLabel(self)
        self.label_book.setGeometry(QtCore.QRect(110, 10, 341, 21))
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(12)
        self.label_book.setFont(font)
        self.label_book.setAlignment(QtCore.Qt.AlignCenter)
        self.label_book.setObjectName("label_book")
        self.pushButton_book_back = QtWidgets.QPushButton(self)
        self.pushButton_book_back.setGeometry(QtCore.QRect(240, 420, 93, 28))
        self.pushButton_book_back.setObjectName("pushButton_book_back")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "book"))
        self.pushButton_book_singong.setText(_translate("Form", "신공학관"))
        self.pushButton_book_haebong.setText(_translate("Form", "해봉관"))
        self.pushButton_book_sanhak.setText(_translate("Form", "산학협동관"))
        self.pushButton_book_gongdae.setText(_translate("Form", "공과대학"))
        self.label_book.setText(_translate("Form", "예약할 주차장을 선택하세요"))
        self.pushButton_book_back.setText(_translate("Form", "돌아가기"))

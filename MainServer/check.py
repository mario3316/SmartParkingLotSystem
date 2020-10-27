# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'check.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class checkUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(checkUI, self).__init__(parent)
        self.setupUi()
    def setupUi(self):
        # disable (but not hide) close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        self.setObjectName("Form")
        self.resize(574, 460)
        self.pushButton_check_singong = QtWidgets.QPushButton(self)
        self.pushButton_check_singong.setGeometry(QtCore.QRect(30, 40, 211, 161))
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(14)
        self.pushButton_check_singong.setFont(font)
        self.pushButton_check_singong.setObjectName("pushButton_check_singong")
        self.pushButton_check_haebong = QtWidgets.QPushButton(self)
        self.pushButton_check_haebong.setGeometry(QtCore.QRect(330, 250, 211, 161))
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(14)
        self.pushButton_check_haebong.setFont(font)
        self.pushButton_check_haebong.setObjectName("pushButton_check_haebong")
        self.pushButton_check_sanhak = QtWidgets.QPushButton(self)
        self.pushButton_check_sanhak.setGeometry(QtCore.QRect(30, 250, 211, 161))
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(14)
        self.pushButton_check_sanhak.setFont(font)
        self.pushButton_check_sanhak.setObjectName("pushButton_check_sanhak")
        self.pushButton_check_gongdae = QtWidgets.QPushButton(self)
        self.pushButton_check_gongdae.setGeometry(QtCore.QRect(330, 40, 211, 161))
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(14)
        self.pushButton_check_gongdae.setFont(font)
        self.pushButton_check_gongdae.setObjectName("pushButton_check_gongdae")
        self.label_check = QtWidgets.QLabel(self)
        self.label_check.setGeometry(QtCore.QRect(110, 10, 341, 21))
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(12)
        self.label_check.setFont(font)
        self.label_check.setAlignment(QtCore.Qt.AlignCenter)
        self.label_check.setObjectName("label_check")
        self.pushButton_check_back = QtWidgets.QPushButton(self)
        self.pushButton_check_back.setGeometry(QtCore.QRect(240, 430, 93, 28))
        self.pushButton_check_back.setObjectName("pushButton_check_back")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "check"))
        self.pushButton_check_singong.setText(_translate("Form", "신공학관"))
        self.pushButton_check_haebong.setText(_translate("Form", "해봉관"))
        self.pushButton_check_sanhak.setText(_translate("Form", "산학협동관"))
        self.pushButton_check_gongdae.setText(_translate("Form", "공과대학"))
        self.label_check.setText(_translate("Form", "조회할 주차장을 선택하세요"))
        self.pushButton_check_back.setText(_translate("Form", "뒤로"))
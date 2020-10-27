# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'admin_main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class admin_mainUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(admin_mainUI, self).__init__(parent)
        self.setupUi()
    def setupUi(self):
        self.setObjectName("Form")
        self.resize(769, 733)
        self.textBrowser_admin_main_log = QtWidgets.QTextBrowser(self)
        self.textBrowser_admin_main_log.setGeometry(QtCore.QRect(30, 50, 701, 371))
        self.textBrowser_admin_main_log.setObjectName("textBrowser_admin_main_log")
        self.label_admin_main_log = QtWidgets.QLabel(self)
        self.label_admin_main_log.setGeometry(QtCore.QRect(40, 20, 161, 21))
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(11)
        self.label_admin_main_log.setFont(font)
        self.label_admin_main_log.setObjectName("label_admin_main_log")
        self.label_admin_main_cur = QtWidgets.QLabel(self)
        self.label_admin_main_cur.setGeometry(QtCore.QRect(40, 440, 161, 21))
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(11)
        self.label_admin_main_cur.setFont(font)
        self.label_admin_main_cur.setObjectName("label_admin_main_cur")
        self.textBrowser_admin_main_log_2 = QtWidgets.QTextBrowser(self)
        self.textBrowser_admin_main_log_2.setGeometry(QtCore.QRect(30, 470, 701, 192))
        self.textBrowser_admin_main_log_2.setObjectName("textBrowser_admin_main_log_2")
        self.pushButton_admin_main_back = QtWidgets.QPushButton(self)
        self.pushButton_admin_main_back.setGeometry(QtCore.QRect(330, 690, 93, 28))
        self.pushButton_admin_main_back.setObjectName("pushButton_admin_main_back")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "admin_main"))
        self.label_admin_main_log.setText(_translate("Form", "<주차장 이용 로그>"))
        self.label_admin_main_cur.setText(_translate("Form", "<접속중인 클라이언트>"))
        self.pushButton_admin_main_back.setText(_translate("Form", "종료"))

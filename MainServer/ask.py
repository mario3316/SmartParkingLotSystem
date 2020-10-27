# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ask.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class askUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(askUI, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        # disable (but not hide) close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        self.setObjectName("Form")
        self.resize(374, 229)
        self.label_ask_book = QtWidgets.QLabel(self)
        self.label_ask_book.setGeometry(QtCore.QRect(20, 40, 331, 31))
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(18)
        self.label_ask_book.setFont(font)
        self.label_ask_book.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ask_book.setObjectName("label_ask_book")
        self.pushButton_ask_yes = QtWidgets.QPushButton(self)
        self.pushButton_ask_yes.setGeometry(QtCore.QRect(70, 150, 111, 31))
        self.pushButton_ask_yes.setObjectName("pushButton_ask_yes")
        self.pushButton_ask_no = QtWidgets.QPushButton(self)
        self.pushButton_ask_no.setGeometry(QtCore.QRect(200, 150, 111, 31))
        self.pushButton_ask_no.setObjectName("pushButton_ask_no")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "ask"))
        self.label_ask_book.setText(_translate("Form", "예약하시겠습니까 ?"))
        self.pushButton_ask_yes.setText(_translate("Form", "예"))
        self.pushButton_ask_no.setText(_translate("Form", "아니요"))

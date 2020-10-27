# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class mainUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(mainUI, self).__init__(parent)
        self.setupUi()
    def setupUi(self):
        self.setObjectName("Form")
        self.resize(771, 487)
        self.pushButton_check = QtWidgets.QPushButton(self)
        self.pushButton_check.setGeometry(QtCore.QRect(140, 260, 181, 141))
        self.pushButton_check.setObjectName("pushButton_check")
        self.label_printID = QtWidgets.QLabel(self)
        self.label_printID.setGeometry(QtCore.QRect(30, 10, 121, 51))
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(13)
        self.label_printID.setFont(font)
        self.label_printID.setObjectName("label_printID")
        self.label_printTitle = QtWidgets.QLabel(self)
        self.label_printTitle.setGeometry(QtCore.QRect(60, 100, 661, 41))
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(20)
        self.label_printTitle.setFont(font)
        self.label_printTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_printTitle.setObjectName("label_printTitle")
        self.pushButton_book = QtWidgets.QPushButton(self)
        self.pushButton_book.setGeometry(QtCore.QRect(450, 260, 181, 141))
        self.pushButton_book.setObjectName("pushButton_book")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "main"))
        self.pushButton_check.setText(_translate("Form", "주차장 조회"))
        self.label_printID.setText(_translate("Form", "ID : xxx"))
        self.label_printTitle.setText(_translate("Form", "Konkuk University Smart Parking Lot"))
        self.pushButton_book.setText(_translate("Form", "주차장 예약"))
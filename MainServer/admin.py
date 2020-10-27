# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class adminUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(adminUI, self).__init__(parent)
        self.setupUi()
    def setupUi(self):
        self.setObjectName("Form")
        self.resize(873, 451)
        self.label_admin = QtWidgets.QLabel(self)
        self.label_admin.setGeometry(QtCore.QRect(80, 30, 721, 261))
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(16)
        self.label_admin.setFont(font)
        self.label_admin.setAlignment(QtCore.Qt.AlignCenter)
        self.label_admin.setObjectName("label_admin")
        self.labe_admin_2 = QtWidgets.QLabel(self)
        self.labe_admin_2.setGeometry(QtCore.QRect(60, 240, 201, 91))
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(12)
        self.labe_admin_2.setFont(font)
        self.labe_admin_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labe_admin_2.setObjectName("labe_admin_2")
        self.textEdit_admin = QtWidgets.QTextEdit(self)
        self.textEdit_admin.setGeometry(QtCore.QRect(80, 350, 461, 87))
        self.textEdit_admin.setObjectName("textEdit_admin")
        self.label_admin_3 = QtWidgets.QLabel(self)
        self.label_admin_3.setGeometry(QtCore.QRect(70, 330, 131, 16))
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(10)
        self.label_admin_3.setFont(font)
        self.label_admin_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_admin_3.setObjectName("label_admin_3")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(560, 350, 141, 81))
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "admin"))
        self.label_admin.setText(_translate("Form", "Welcome to Konkuk University Smart Parking Lot System"))
        self.labe_admin_2.setText(_translate("Form", "for Administrator"))
        self.label_admin_3.setText(_translate("Form", "<PassWord>"))
        self.pushButton.setText(_translate("Form", "접속"))
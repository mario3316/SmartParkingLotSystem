# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'book_haebong.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class book_haebongUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(book_haebongUI, self).__init__(parent)
        self.setupUi()
    def setupUi(self):
        # disable (but not hide) close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        self.setObjectName("Form")
        self.resize(607, 654)
        self.label_book_haebong = QtWidgets.QLabel(self)
        self.label_book_haebong.setGeometry(QtCore.QRect(220, 40, 171, 41))
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(26)
        self.label_book_haebong.setFont(font)
        self.label_book_haebong.setAlignment(QtCore.Qt.AlignCenter)
        self.label_book_haebong.setObjectName("label_book_haebong")
        self.label_book_B1_haebong = QtWidgets.QLabel(self)
        self.label_book_B1_haebong.setGeometry(QtCore.QRect(40, 150, 61, 41))
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(18)
        self.label_book_B1_haebong.setFont(font)
        self.label_book_B1_haebong.setObjectName("label_book_B1_haebong")
        self.label_book_B2_haebong = QtWidgets.QLabel(self)
        self.label_book_B2_haebong.setGeometry(QtCore.QRect(40, 280, 61, 41))
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(18)
        self.label_book_B2_haebong.setFont(font)
        self.label_book_B2_haebong.setObjectName("label_book_B2_haebong")
        self.listWidget_book_B1_haebong = QtWidgets.QListWidget(self)
        self.listWidget_book_B1_haebong.setGeometry(QtCore.QRect(140, 120, 411, 101))
        self.listWidget_book_B1_haebong.setFlow(QtWidgets.QListView.LeftToRight)
        self.listWidget_book_B1_haebong.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget_book_B1_haebong.setGridSize(QtCore.QSize(80, 0))
        self.listWidget_book_B1_haebong.setObjectName("listWidget_book_B1_haebong")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(11)
        item.setFont(font)
        self.listWidget_book_B1_haebong.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(11)
        item.setFont(font)
        self.listWidget_book_B1_haebong.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(11)
        item.setFont(font)
        self.listWidget_book_B1_haebong.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(11)
        item.setFont(font)
        self.listWidget_book_B1_haebong.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(11)
        item.setFont(font)
        self.listWidget_book_B1_haebong.addItem(item)
        self.listWidget_book_B2_haebong = QtWidgets.QListWidget(self)
        self.listWidget_book_B2_haebong.setGeometry(QtCore.QRect(140, 250, 411, 101))
        self.listWidget_book_B2_haebong.setFlow(QtWidgets.QListView.LeftToRight)
        self.listWidget_book_B2_haebong.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget_book_B2_haebong.setGridSize(QtCore.QSize(80, 0))
        self.listWidget_book_B2_haebong.setObjectName("listWidget_book_B2_haebong")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(11)
        item.setFont(font)
        self.listWidget_book_B2_haebong.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(11)
        item.setFont(font)
        self.listWidget_book_B2_haebong.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(11)
        item.setFont(font)
        self.listWidget_book_B2_haebong.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(11)
        item.setFont(font)
        self.listWidget_book_B2_haebong.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("-2002")
        font.setPointSize(11)
        item.setFont(font)
        self.listWidget_book_B2_haebong.addItem(item)
        self.pushButton_book_haebong_back = QtWidgets.QPushButton(self)
        self.pushButton_book_haebong_back.setGeometry(QtCore.QRect(260, 560, 93, 28))
        self.pushButton_book_haebong_back.setObjectName("pushButton_book_haebong_back")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "check_haebong"))
        self.label_book_haebong.setText(_translate("Form", "해봉관"))
        self.label_book_B1_haebong.setText(_translate("Form", "B1"))
        self.label_book_B2_haebong.setText(_translate("Form", "B2"))
        __sortingEnabled = self.listWidget_book_B1_haebong.isSortingEnabled()
        self.listWidget_book_B1_haebong.setSortingEnabled(False)
        item = self.listWidget_book_B1_haebong.item(0)
        item.setText(_translate("Form", "      0      "))
        item = self.listWidget_book_B1_haebong.item(1)
        item.setText(_translate("Form", "      1      "))
        item = self.listWidget_book_B1_haebong.item(2)
        item.setText(_translate("Form", "      2      "))
        item = self.listWidget_book_B1_haebong.item(3)
        item.setText(_translate("Form", "      3      "))
        item = self.listWidget_book_B1_haebong.item(4)
        item.setText(_translate("Form", "      4      "))
        self.listWidget_book_B1_haebong.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_book_B2_haebong.isSortingEnabled()
        self.listWidget_book_B2_haebong.setSortingEnabled(False)
        item = self.listWidget_book_B2_haebong.item(0)
        item.setText(_translate("Form", "      0      "))
        item = self.listWidget_book_B2_haebong.item(1)
        item.setText(_translate("Form", "      1      "))
        item = self.listWidget_book_B2_haebong.item(2)
        item.setText(_translate("Form", "      2      "))
        item = self.listWidget_book_B2_haebong.item(3)
        item.setText(_translate("Form", "      3      "))
        item = self.listWidget_book_B2_haebong.item(4)
        item.setText(_translate("Form", "      4      "))
        self.listWidget_book_B2_haebong.setSortingEnabled(__sortingEnabled)
        self.pushButton_book_haebong_back.setText(_translate("Form", "돌아가기"))
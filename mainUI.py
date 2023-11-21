# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ManageWindow(object):
    def setupUi(self, ManageWindow):
        ManageWindow.setObjectName("ManageWindow")
        ManageWindow.resize(1200, 640)
        ManageWindow.setStyleSheet("QPushButton\n"
"{\n"
"    corlor: white;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(ManageWindow)
        self.centralwidget.setStyleSheet("background-color: rgba(34, 44, 58, 1);")
        self.centralwidget.setObjectName("centralwidget")
        self.OpenMessageEncription = QtWidgets.QPushButton(self.centralwidget)
        self.OpenMessageEncription.setGeometry(QtCore.QRect(660, 290, 500, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.OpenMessageEncription.setFont(font)
        self.OpenMessageEncription.setStyleSheet("background-color: rgba(72, 199, 166, 1);\n"
"color: white;\n"
"border-radius: 5px;\n"
"\n"
"QPushButton::hover\n"
"{\n"
"    \n"
"    background-color: rgb(135, 255, 71);\n"
"}")
        self.OpenMessageEncription.setObjectName("OpenMessageEncription")
        self.OpenFilesEncription = QtWidgets.QPushButton(self.centralwidget)
        self.OpenFilesEncription.setGeometry(QtCore.QRect(50, 295, 500, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.OpenFilesEncription.setFont(font)
        self.OpenFilesEncription.setStyleSheet("background-color: rgba(72, 199, 166, 1);\n"
"color: white;\n"
"border-radius: 5px;")
        self.OpenFilesEncription.setObjectName("OpenFilesEncription")
        self.OpenHistoryEncription = QtWidgets.QPushButton(self.centralwidget)
        self.OpenHistoryEncription.setGeometry(QtCore.QRect(345, 425, 500, 100))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.OpenHistoryEncription.setFont(font)
        self.OpenHistoryEncription.setStyleSheet("background-color: rgba(41, 72, 109, 1);\n"
"color: white;\n"
"border-radius: 5px;")
        self.OpenHistoryEncription.setObjectName("OpenHistoryEncription")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 30, 451, 231))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/Logo_MainW.png"))
        self.label.setObjectName("label")
        ManageWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ManageWindow)
        QtCore.QMetaObject.connectSlotsByName(ManageWindow)

    def retranslateUi(self, ManageWindow):
        _translate = QtCore.QCoreApplication.translate
        ManageWindow.setWindowTitle(_translate("ManageWindow", "ManageWindow"))
        self.OpenMessageEncription.setText(_translate("ManageWindow", "Шифрование сообщений"))
        self.OpenFilesEncription.setText(_translate("ManageWindow", "Шифрование файлов"))
        self.OpenHistoryEncription.setText(_translate("ManageWindow", "История шифрований"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ManageWindow = QtWidgets.QMainWindow()
    ui = Ui_ManageWindow()
    ui.setupUi(ManageWindow)
    ManageWindow.show()
    sys.exit(app.exec_())

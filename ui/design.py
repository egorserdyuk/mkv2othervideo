# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 368)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 260, 151, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 260, 151, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 260, 151, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 230, 151, 31))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(610, 230, 151, 31))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 220, 741, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(40, 10, 721, 181))
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "mkv2othervideo - open source video decoder"))
        self.pushButton.setText(_translate("MainWindow", "Select video"))
        self.pushButton_2.setText(_translate("MainWindow", "Convert"))
        self.pushButton_3.setText(_translate("MainWindow", "Select output folder"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">mkv2othervideo is open source software which can be used by anyone under the MIT license.</span></p><p><span style=\" font-size:10pt;\">This software uses the ffmpeg library which is distributed under the GNU Lesser General Public License version 2.1 or later <br> (LGPL v2.1+). The website of the project is </span><a href=\"https://ffmpeg.org/\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">https://ffmpeg.org/</span></a></p><p><span style=\" font-size:10pt;\">This software uses the graphical system Qt (in particular PyQt5 licensed under the GNU GPL v3 and the Riverbank Commercial <br>  License, the project website </span><a href=\"https://riverbankcomputing.com/\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">https://riverbankcomputing.com/</span></a><span style=\" font-size:10pt;\">) distributed under the Free Software Foundation open license <br> (</span><a href=\"https://www.qt.io/licensing/\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">https://www.qt.io/licensing/</span></a><span style=\" font-size:10pt;\">), the project website </span><a href=\"https://www.qt.io/\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">https://www.qt.io/</span></a></p><p><span style=\" font-size:10pt;\">This program will always contain open source and complies with the MIT license, does not collect data and was created to <br> help my friend who practices in the field of video editing.</span></p></body></html>"))

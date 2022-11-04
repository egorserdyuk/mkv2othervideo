# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
                               QProgressBar, QPushButton, QSizePolicy, QStatusBar,
                               QWidget, QDialog, QFrame)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(926, 194)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QRect(10, 10, 911, 181))
        self.label_3.setFrameShadow(QFrame.Plain)
        self.label_3.setTextFormat(Qt.AutoText)
        self.label_3.setScaledContents(False)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"About", None))
        self.label_3.setText(QCoreApplication.translate("Dialog",
                                                        u"<html><head/><body><p><span style=\" font-size:10pt;\">mkv2othervideo is open source software which can be used by anyone under the MIT license.</span></p><p><span style=\" font-size:10pt;\">This software uses the ffmpeg library which is distributed under the GNU Lesser General Public License version 2.1 or later <br/>(LGPL v2.1+). The website of the project is </span><a href=\"https://ffmpeg.org/\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">https://ffmpeg.org/</span></a></p><p><span style=\" font-size:10pt;\">This software uses the PySide6 graphical system (licensed under the LGPL, developed by The Qt Company, project website </span><a href=\"https://www.qt.io/qt-for-python\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">https://www.qt.io/qt-for-python</span></a><span style=\" font-size:10pt;\">).</span></p><p><span style=\" font-size:10pt;\">This program will always contain open source and complies with the MIT license, does not collect data and "
                                                        "was created to <br/>help my friend who practices in the field of video editing.</span></p><p><a href=\"https://github.com/egorserdyuk\"><span style=\" text-decoration: underline; color:#0000ff;\">Egor Serdiuk</span></a><span style=\" font-size:10pt;\">, 2022</span></p></body></html>",
                                                        None))
    # retranslateUi


class Ui_MainWindow(object):
    def openDialog(self):
        self.window = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(796, 173)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAbout.setCheckable(True)
        self.actionAbout.setChecked(False)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 60, 151, 61))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(580, 60, 151, 61))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(210, 60, 151, 61))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 230, 151, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(610, 230, 151, 31))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 20, 741, 23))
        self.progressBar.setValue(24)
        self.pushButton_4 = QPushButton(self.centralwidget, clicked=lambda: self.openDialog())
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(400, 60, 151, 61))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 796, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"mkv2othervideo - open source video decoder", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Select video", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Select output folder", None))
        self.label.setText("")
        self.label_2.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

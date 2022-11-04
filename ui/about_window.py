# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
                               QSizePolicy, QWidget)


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

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainAcxfAc.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTabWidget,
    QWidget)

class Ui_Timer(object):
    def setupUi(self, Timer):
        if not Timer.objectName():
            Timer.setObjectName(u"Timer")
        Timer.setEnabled(True)
        Timer.resize(185, 45)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Timer.sizePolicy().hasHeightForWidth())
        Timer.setSizePolicy(sizePolicy)
        Timer.setMinimumSize(QSize(185, 45))
        Timer.setMaximumSize(QSize(185, 45))
        Timer.setAutoFillBackground(False)
        Timer.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        Timer.setAnimated(True)
        Timer.setTabShape(QTabWidget.Rounded)
        Timer.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.centralwidget = QWidget(Timer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(-1, -1, 181, 41))
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.timeInput = QLineEdit(self.page1)
        self.timeInput.setObjectName(u"timeInput")
        self.timeInput.setGeometry(QRect(10, 10, 101, 30))
        self.timeInput.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.startButton = QPushButton(self.page1)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(119, 10, 31, 31))
        font = QFont()
        font.setPointSize(10)
        self.startButton.setFont(font)
        self.startButton.setStyleSheet(u"background-color: rgb(100, 100, 100);")
        self.exitButton = QPushButton(self.page1)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setEnabled(True)
        self.exitButton.setGeometry(QRect(150, 10, 31, 31))
        sizePolicy.setHeightForWidth(self.exitButton.sizePolicy().hasHeightForWidth())
        self.exitButton.setSizePolicy(sizePolicy)
        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet(u"background-color: rgb(100, 100, 100);")
        self.stackedWidget.addWidget(self.page1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.exitButton2 = QPushButton(self.page_2)
        self.exitButton2.setObjectName(u"exitButton2")
        self.exitButton2.setEnabled(True)
        self.exitButton2.setGeometry(QRect(150, 10, 31, 31))
        sizePolicy.setHeightForWidth(self.exitButton2.sizePolicy().hasHeightForWidth())
        self.exitButton2.setSizePolicy(sizePolicy)
        self.exitButton2.setFont(font)
        self.exitButton2.setStyleSheet(u"background-color: rgb(100, 100, 100);")
        self.minutes_text = QLabel(self.page_2)
        self.minutes_text.setObjectName(u"minutes_text")
        self.minutes_text.setGeometry(QRect(10, 10, 131, 31))
        self.minutes_text.setStyleSheet(u"color: rgb(255,255,255);")
        self.stackedWidget.addWidget(self.page_2)
        Timer.setCentralWidget(self.centralwidget)

        self.retranslateUi(Timer)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Timer)
    # setupUi

    def retranslateUi(self, Timer):
        Timer.setWindowTitle(QCoreApplication.translate("Timer", u"Timer", None))
        self.timeInput.setText("")
        self.timeInput.setPlaceholderText(QCoreApplication.translate("Timer", u"Enter min", None))
        self.startButton.setText(QCoreApplication.translate("Timer", u"\u2705", None))
        self.exitButton.setText(QCoreApplication.translate("Timer", u"\u274c", None))
        self.exitButton2.setText(QCoreApplication.translate("Timer", u"\u274c", None))
        self.minutes_text.setText("")
    # retranslateUi


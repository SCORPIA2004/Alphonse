# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testSgHohU.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QLCDNumber, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.resize(219, 121)
        self.actionWhat_am_I_doing = QAction(MainWindow)
        self.actionWhat_am_I_doing.setObjectName(u"actionWhat_am_I_doing")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.seconds = QLCDNumber(self.centralwidget)
        self.seconds.setObjectName(u"seconds")
        self.seconds.setGeometry(QRect(170, 40, 31, 23))
        self.seconds.setDigitCount(2)
        self.pushButton_incr = QPushButton(self.centralwidget)
        self.pushButton_incr.setObjectName(u"pushButton_incr")
        self.pushButton_incr.setGeometry(QRect(40, 40, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionWhat_am_I_doing.setText(QCoreApplication.translate("MainWindow", u"What am I doing", None))
        self.pushButton_incr.setText(QCoreApplication.translate("MainWindow", u"Increment", None))
    # retranslateUi


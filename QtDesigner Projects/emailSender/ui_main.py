# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainKVGOes.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(501, 322)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(300, 150))
        MainWindow.setMaximumSize(QSize(501, 322))
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: #222222;\n"
"    color: #ffffff;\n"
"    font-family: \"Roboto\", sans-serif;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #333333;\n"
"    color: #ffffff;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #444444;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #333333;\n"
"    color: #ffffff;\n"
"    border: 1px solid #444444;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QTextEdit {\n"
"    background-color: #333333;\n"
"    color: #ffffff;\n"
"    border: 1px solid #444444;\n"
"    padding: 10px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.lineEditBody = QLineEdit(self.page)
        self.lineEditBody.setObjectName(u"lineEditBody")
        self.lineEditBody.setGeometry(QRect(-5, 94, 483, 170))
        self.lineEditBody.setMinimumSize(QSize(0, 170))
        self.lineEditBody.setReadOnly(False)
        self.pushButtonSend = QPushButton(self.page)
        self.pushButtonSend.setObjectName(u"pushButtonSend")
        self.pushButtonSend.setGeometry(QRect(-5, 270, 239, 36))
        self.pushButtonSend.setMinimumSize(QSize(50, 0))
        self.pushButtonSend.setMaximumSize(QSize(16777215, 40))
        self.lineEditEmail = QLineEdit(self.page)
        self.lineEditEmail.setObjectName(u"lineEditEmail")
        self.lineEditEmail.setGeometry(QRect(-5, 2, 483, 40))
        self.lineEditEmail.setMinimumSize(QSize(0, 30))
        self.lineEditSubject = QLineEdit(self.page)
        self.lineEditSubject.setObjectName(u"lineEditSubject")
        self.lineEditSubject.setGeometry(QRect(-5, 48, 483, 40))
        self.lineEditSubject.setMinimumSize(QSize(0, 30))
        self.pushButtonReset = QPushButton(self.page)
        self.pushButtonReset.setObjectName(u"pushButtonReset")
        self.pushButtonReset.setGeometry(QRect(240, 270, 238, 36))
        self.pushButtonReset.setMaximumSize(QSize(16777215, 40))
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_2 = QGridLayout(self.page_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)

        self.pushButtonExit = QPushButton(self.page_3)
        self.pushButtonExit.setObjectName(u"pushButtonExit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButtonExit.sizePolicy().hasHeightForWidth())
        self.pushButtonExit.setSizePolicy(sizePolicy1)
        self.pushButtonExit.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.pushButtonExit, 1, 0, 1, 1)

        self.pushButtonNew = QPushButton(self.page_3)
        self.pushButtonNew.setObjectName(u"pushButtonNew")
        sizePolicy1.setHeightForWidth(self.pushButtonNew.sizePolicy().hasHeightForWidth())
        self.pushButtonNew.setSizePolicy(sizePolicy1)
        self.pushButtonNew.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.pushButtonNew, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_3)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Email Sender", None))
        self.lineEditBody.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Body", None))
        self.pushButtonSend.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.lineEditEmail.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lineEditSubject.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Subject", None))
        self.pushButtonReset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Email sent", None))
        self.pushButtonExit.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.pushButtonNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
    # retranslateUi


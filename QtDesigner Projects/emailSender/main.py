import sys
# from layout_colorwidget import Color
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import QScreen
from ui_main import Ui_MainWindow
import smtplib
import csv
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Fill in the details for your email account
sender_email = "mshayanalwaha@gmail.com"
app_password = "uluaskwkgccmjgxr"

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(sender_email, app_password)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        # self.setWindowFlag(Qt.FramelessWindowHint)

        # screenWidth = app.primaryScreen().size().width()
        # self.setGeometry(screenWidth - 247, 0, 185, 45)
        self.ui.setupUi(self)
        self.receiverEmail = ""
        self.subject = ""
        self.body = ""

        self.ui.pushButtonSend.clicked.connect(self.sendEmail)
        self.ui.pushButtonReset.clicked.connect(self.reset)
        self.ui.lineEditEmail.textChanged.connect(self.setReceiverEmail)
        self.ui.lineEditSubject.textChanged.connect(self.setSubject)
        self.ui.lineEditBody.textChanged.connect(self.setBody)
        self.ui.pushButtonExit.clicked.connect(self.exitApp)
        self.ui.pushButtonNew.clicked.connect(self.newEmail)
        self.ui.stackedWidget.setCurrentIndex(0)


    def sendEmail(self):
        message = MIMEMultipart()

        # Add the body of the email to the MIME message

        # message.attach(self.body)
        body = MIMEText(self.body)
        message.attach(body)

        # Add the attachment to the MIME message
        with open("Muhammad Shayan Resume.pdf", "rb") as f:
            attach = MIMEApplication(f.read(), _subtype="pdf")
            attach.add_header("Content-Disposition", "attachment", filename="Muhammad Shayan Usman Resume.pdf")
            message.attach(attach)

        message["Subject"] = self.subject
        message["From"] = sender_email
        message["To"] = self.receiverEmail

        receipientEmails = [self.receiverEmail]

        server.sendmail(sender_email, receipientEmails, message.as_string())
        print(f"Sent email to {self.receiverEmail}")
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.label.setText(f"Sent email to {self.receiverEmail}")

    def newEmail(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.reset()

    def setReceiverEmail(self, str):
        self.receiverEmail = str

    def setSubject(self, str):
        self.subject = str

    def setBody(self, str):
        self.body = str

    def reset(self):
        self.ui.lineEditEmail.setText("")
        self.ui.lineEditSubject.setText("")
        self.ui.lineEditBody.setText("")

    def exitApp(self):
        server.quit()
        QCoreApplication.instance().quit()




app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
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

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        self.receiverEmail = ""
        self.subject = ""
        self.body = ""
        self.filename = ""
        self.batch = False

        self.ui.pushButtonSend.clicked.connect(self.sendEmail)
        self.ui.pushButtonReset.clicked.connect(self.reset)

        self.ui.lineEditEmail.textChanged.connect(self.setReceiverEmail)
        self.ui.lineEditSubject.textChanged.connect(self.setSubject)
        self.ui.lineEditBody.textChanged.connect(self.setBody)

        self.ui.pushButtonExit.clicked.connect(self.exitApp)
        self.ui.pushButtonNew.clicked.connect(self.goToSingleOrBatchPage)

        self.ui.pushButtonBatch.clicked.connect(self.goToUploadPage)
        self.ui.pushButtonUpload.clicked.connect(self.uploadFile)
        self.ui.pushButtonCompose.clicked.connect(self.newEmail)
        self.ui.pushButtonSingle.clicked.connect(self.newEmail)

        self.ui.stackedWidget.setCurrentIndex(0)

    def sendEmail(self):
        if self.batch:
            print("Sending batch")
            self.batchSend()
        else:
            message = MIMEMultipart()


            body = MIMEText(self.body)
            message.attach(body)

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
            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.labelEmailSent.setText(f"Sent single email to {self.receiverEmail}")

    def goToUploadPage(self):
        self.batch = True
        self.ui.stackedWidget.setCurrentIndex(1)

    def goToSingleOrBatchPage(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def newEmail(self):
        self.ui.stackedWidget.setCurrentIndex(2)
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
        self.receiverEmail = ""
        self.subject = ""
        self.body = ""

    def exitApp(self):
        server.quit()
        QCoreApplication.instance().quit()

    def uploadFile(self):
        filenameArr, selectedFilter = QFileDialog.getOpenFileNames(self)
        self.filename = filenameArr[0]
        self.ui.labelFileName.setText(self.filename)


    def batchSend(self):
        recipients = []

        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                recipients.append(row[0])

        count = 0

        for recipient in recipients:
            count += 1
            message = MIMEMultipart()

            body = MIMEText(self.body)
            message.attach(body)

            # Add the attachment to the MIME message
            with open("Muhammad Shayan Resume.pdf", "rb") as f:
                attach = MIMEApplication(f.read(), _subtype="pdf")
                attach.add_header("Content-Disposition", "attachment", filename="Muhammad Shayan Usman Resume.pdf")
                message.attach(attach)

            message["Subject"] = self.subject
            message["From"] = sender_email
            message["To"] = recipient

            # receipientEmails = [self.receiverEmail]

            server.sendmail(sender_email, recipient, message.as_string())
            print(f"Sent email to {recipient}")

        self.ui.labelEmailSent.setText(f"Sent email to {count} recipients")
        self.ui.stackedWidget.setCurrentIndex(3)
        self.batch = False


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
import sys,os
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton
from PySide6.QtGui import QPixmap

basedir = os.path.dirname(__file__)
print("current dir: ", os.getcwd())
print("paths are relative to: ", basedir)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("sssssss")

        widget = QLabel("Hello image")
        widget.setPixmap(QPixmap(os.path.join(basedir, "download.png")))
        widget.setScaledContents(True)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.setMinimumSize(100,100)
window.show()

app.exec()
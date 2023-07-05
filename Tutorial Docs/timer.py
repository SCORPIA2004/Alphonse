import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton
from PySide6.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Timer")

        timerLabel = QLabel("Hello image")

        self.setCentralWidget(timerLabel)

app = QApplication(sys.argv)

window = MainWindow()
window.setFixedSize(100,50)
x_pos = 1758
y_pos = 0
window.move(x_pos, y_pos)

window.show()

app.exec()

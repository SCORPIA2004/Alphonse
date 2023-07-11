import sys
from layout_colorwidget import Color
from PySide6.QtCore import *
from PySide6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Boilerplate code")
        sampleLabel = QLabel("Upload file")

        self.setCentralWidget(sampleLabel)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

import sys
from layout_colorwidget import Color
from PySide6.QtCore import *
from PySide6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Boilerplate code")
        layout = QGridLayout()

        layout.addWidget(Color("red"),0,0)
        layout.addWidget(Color("green"),0,1)
        layout.addWidget(Color("blue"),1,0)
        layout.addWidget(Color("yellow"),2,1)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

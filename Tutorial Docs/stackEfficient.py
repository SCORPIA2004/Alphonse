import sys
from layout_colorwidget import Color
from PySide6.QtCore import *
from PySide6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Boilerplate code")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.North)
        tabs.setMovable(True)

        for n,color in enumerate(["blue", "yellow", "green", "red"]):
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

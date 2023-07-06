import sys

from PySide6.QtGui import QAction

from layout_colorwidget import Color
from PySide6.QtCore import *
from PySide6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Boilerplate code")
        sampleLabel = QLabel("Boilerplate code")
        sampleLabel.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(sampleLabel)

        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

        buttonAction = QAction("My button", self)
        buttonAction.setStatusTip("This is your button")
        buttonAction.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(buttonAction)


    def onMyToolBarButtonClick(self,s):
            print("click", s)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

from time import sleep

from PySide6.QtWidgets import (
  QApplication,
  QHBoxLayout,
  QLabel,
  QMainWindow,
  QPushButton,
  QStackedLayout,
  QVBoxLayout,
  QWidget,
)
from PySide6.QtCore import Qt, QSize
from layout_colorwidget import Color
import sys

class MainWindow(QMainWindow):
    def setSizeOfWindow(self):
        screen = app.primaryScreen()
        screenGeometry = screen.geometry()

        width = screenGeometry.width() / 2
        height = screenGeometry.height() / 2
        self.setFixedSize(QSize(width, height))          # Width, Height

        # self.setFixedSize(QSize(960, 540))          # Width, Height
        self.setMinimumSize(QSize(300, 300))          # Width, Height
        self.setMaximumSize(QSize(1000, 1000))        # Width, Height

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        # create layouts. pageLayout: main layout, buttonLayout: layout for buttons
        pagelayout = QVBoxLayout()
        buttonLayout = QHBoxLayout()
        self.stacklayout = QStackedLayout()

        # set the layout
        pagelayout.addLayout(buttonLayout)
        pagelayout.addLayout(self.stacklayout)

        self.stacklayout.addWidget(Color("red"))
        self.stacklayout.addWidget(Color("blue"))
        self.stacklayout.addWidget(Color("green"))
        self.stacklayout.addWidget(Color("yellow"))

        # set the layout
        container = QWidget()
        container.setLayout(pagelayout)
        self.setCentralWidget(container)

    def onRedButtonPressed(self):
        self.stacklayout.setCurrentIndex(0)

    def onGreenButtonPressed(self):
        self.stacklayout.setCurrentIndex(1)

    def onBlueButtonPressed(self):
        self.stacklayout.setCurrentIndex(2)

    def onYellowButtonPressed(self):
        self.stacklayout.setCurrentIndex(3)


    # layout = QStackedLayout()
    # layout.addWidget(Color("red"))
    # layout.addWidget(Color("green"))
    # layout.addWidget(Color("blue"))
    # layout.addWidget(Color("yellow"))
    #
    # layout.setCurrentIndex(0)
    #
    # container = QWidget()
    # container.setLayout(layout)
    # self.setCentralWidget(container)

app = QApplication(sys.argv)


window = MainWindow()
window.show()

for i in range(1, 5):
    sleep(1)
    window.autoFillBackground()

app.exec()

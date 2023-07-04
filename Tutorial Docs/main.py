from PySide6.QtCore import (
    QSize,
    Qt,
)
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QMainWindow,
)


import sys
from random import choice

windowTitles = [
    "1",
    "2",
    "3",
    "4",
    "5",
]
class MainWindow(QMainWindow):
    # When you subclass a Qt class you must always call the super
    # __init__ function to allow Qt to set up the object.
    def __init__(self):
        super().__init__()

        self.setSizeOfWindow()
        self.setWindowTitle("Hello World of QT via PySide6")

        self.buttonIsChecked = True

        self.button = QPushButton("Click here")
        self.button.clicked.connect(self.buttonWasClicked)
        # self.windowTitleChanged.connect()
        # sets button as central widget of main window
        self.setCentralWidget(self.button)



    def buttonWasReleased(self):
        self.buttonIsChecked = self.button.isChecked()
        print(self.buttonIsChecked)
    def buttonWasClicked(self):
        print("Changing title...")
        newWindowTitle = choice(windowTitles)
        self.setWindowTitle(newWindowTitle)
        if newWindowTitle == "5":
            self.button.setDisabled(True)
            self.button.setText("Disabled")
    def setSizeOfWindow(self):
        screen = app.primaryScreen()
        screenGeometry = screen.geometry()

        width = screenGeometry.width() / 2
        height = screenGeometry.height() / 2
        self.setFixedSize(QSize(width, height))          # Width, Height

        # self.setFixedSize(QSize(960, 540))          # Width, Height
        self.setMinimumSize(QSize(300, 300))          # Width, Height
        self.setMaximumSize(QSize(1000, 1000))        # Width, Height



# Need atleast 1 QApplication instance per application
# sys.argv passed as parameter only to allow cmd line args
app = QApplication(sys.argv)

# Create window as an instance of Qt Widget
# window = QWidget()
mainWindow = MainWindow()
mainWindow.show()               # window is hidden by default

# Start event loop
app.exec()

print("App has been closed")

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

class MainWindow(QMainWindow):
    # When you subclass a Qt class you must always call the super
    # __init__ function to allow Qt to set up the object.
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World of QT via PySide6")
        button = QPushButton("Click here")

        self.setFixedSize(QSize(1920, 1080))          # Width, Height
        self.setMinimumSize(QSize(300, 300))          # Width, Height
        self.setMaximumSize(QSize(1000, 1000))        # Width, Height

        # sets button as central widget of main window
        self.setCentralWidget(button)


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

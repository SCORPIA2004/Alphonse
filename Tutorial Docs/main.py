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

        screen = app.primaryScreen()
        screenGeometry = screen.geometry()

        self.setWindowTitle("Hello World of QT via PySide6")
        button = QPushButton("Click here")
        button.setCheckable(True)
        button.clicked.connect(self.buttonWasClicked)

        width = screenGeometry.width() / 2
        height = screenGeometry.height() / 2
        self.setFixedSize(QSize(width, height))          # Width, Height


        # self.setFixedSize(QSize(960, 540))          # Width, Height
        self.setMinimumSize(QSize(300, 300))          # Width, Height
        self.setMaximumSize(QSize(1000, 1000))        # Width, Height

        # sets button as central widget of main window
        self.setCentralWidget(button)

    def buttonWasClicked(self):
        print("Closing app")
        app.quit()


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

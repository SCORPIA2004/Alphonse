import sys
from layout_colorwidget import Color
from PySide6.QtCore import *
from PySide6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Boilerplate code")
        dialogButton = QPushButton("Press")
        dialogButton.clicked.connect(self.buttonClicked)

        self.setCentralWidget(dialogButton)

    def buttonClicked(self, s):
        print("clicked", s)

        dialog = QDialog(self)
        dialog.setWindowTitle("why")
        dialog.exec()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

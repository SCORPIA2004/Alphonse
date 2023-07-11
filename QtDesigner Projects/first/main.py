import sys
# from layout_colorwidget import Color
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from ui.ui_test import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        # super().__init__()
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.i = 0
        self.ui.pushButton_incr.clicked.connect(self.incr)

    def incr(self):
        self.i = self.i + 1
        self.ui.seconds.display(self.i)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
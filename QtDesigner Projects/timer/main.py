import sys
# from layout_colorwidget import Color
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import QScreen 
from ui_main import Ui_Timer


class MainWindow(QMainWindow):
    def __init__(self):
        # super().__init__()
        QMainWindow.__init__(self)
        self.ui = Ui_Timer()
        self.setWindowFlag(Qt.FramelessWindowHint)

        screenWidth = app.primaryScreen().size().width()
        self.setGeometry(screenWidth - 247, 0, 185, 45)
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.startButton.clicked.connect(self.startTimer)
        self.ui.exitButton.clicked.connect(self.exitApp)
        self.ui.exitButton2.clicked.connect(self.exitApp)
        self.ui.timeInput.textChanged.connect(self.timeInputFunc)

    def startTimer(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def exitApp(self):
        QCoreApplication.instance().quit()
    def timeInputFunc(self, s):
        minutesInput = int(s)
    def start_countdown(self):

        if minutes_text.isdigit():
            self.minutes = int(minutes_text)
            self.seconds_remaining = self.minutes * 60

            # Start the countdown timer
            self.timer.start(1000)

            # Disable input and start button
            self.minutes_input.setEnabled(False)
            self.start_button.setEnabled(False)
            self.minutes_label.hide()
            self.start_button.hide()
            self.minutes_input.hide()

    def update_timer(self):
        self.seconds_remaining -= 1
        self.update()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
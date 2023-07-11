import sys, os

from PySide6.QtGui import QAction, QIcon

from layout_colorwidget import Color
from PySide6.QtCore import *
from PySide6.QtWidgets import *

basedir = os.path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Boilerplate code")
        sampleLabel = QLabel("Boilerplate code")
        sampleLabel.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(sampleLabel)

        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

        buttonAction = QAction(QIcon(os.path.join(basedir, "logo.ico")),"My button", self)
        buttonAction.setStatusTip("Taskbar button was clicked")
        buttonAction.triggered.connect(self.onMyToolBarButtonClick)
        buttonAction.setCheckable(True)
        # buttonAction.setEnabled(buttonAction.isChecked())
        toolbar.addAction(buttonAction)
        toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.setStatusBar(QStatusBar(self))
    def onMyToolBarButtonClick(self,s):
            print("click", s)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

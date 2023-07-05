import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox, QLineEdit, QVBoxLayout, QWidget
from PySide6.QtCore import Qt, QSize




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setSizeOfWindow()
        self.setWindowTitle("Combo")

        # Combo box
        self.combo = QComboBox()
        self.combo.addItems(["Fire", "Destructive", "Ice", "Healing", "philosopher's stone"])
        self.combo.currentIndexChanged.connect(self.indexChanged)
        self.combo.currentTextChanged.connect(self.textChanged)

        # input field
        self.inputField = QLineEdit()
        self.inputField.setMaxLength(10)
        self.inputField.setPlaceholderText("Enter choice")

        self.inputField.returnPressed.connect(self.returnPressed)
        self.inputField.selectionChanged.connect(self.selectionChanged)
        self.inputField.textChanged.connect(self.textChanged)
        self.inputField.textEdited.connect(self.textEdited)

        layout = QVBoxLayout()
        layout.addWidget(self.combo)
        layout.addWidget(self.inputField)

        container = QWidget()
        container.setLayout(layout)
        container.setMaximumSize(200, 100)

        self.setCentralWidget(container)
    def indexChanged(self, index):
        print(index)
    def textChanged(self, str):
        print(str)

    def returnPressed(self):
        print("Return pressed")
        self.centralWidget.setText("Return pressed")

    def selectionChanged(self):
        print("Selection changed")
        print(self.centralWidget.selectedText())
    def textEdited(self, str):
        print("Text edited")
        print(str)
    def textChanged(self, str):
        print("Text changed")
        print(str)
    def setSizeOfWindow(self):
        screen = app.primaryScreen()
        screenGeometry = screen.geometry()

        width = screenGeometry.width() / 2
        height = screenGeometry.height() / 2
        self.setFixedSize(QSize(width, height))  # Width, Height

        # self.setFixedSize(QSize(960, 540))          # Width, Height
        self.setMinimumSize(QSize(300, 300))  # Width, Height
        self.setMaximumSize(QSize(1000, 1000))  # Width, Height

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
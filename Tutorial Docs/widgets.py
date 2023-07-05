import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton
from PySide6.QtGui import QFont, QFontDatabase, QGradient, QBrush, QPalette, QLinearGradient


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
        self.setSizeOfWindow()
        self.setWindowTitle("Widgets tests")

        wLabel= QLabel("This is a label")
        wLabel.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(wLabel)


class SignInWindow(QMainWindow):
    def setSizeOfWindow(self):
        screen = app.primaryScreen()
        screenGeometry = screen.geometry()

        width = screenGeometry.width() / 3
        height = screenGeometry.height() / 3
        self.setFixedSize(QSize(width, height))  # Width, Height

        # self.setFixedSize(QSize(960, 540))          # Width, Height
        self.setMinimumSize(QSize(300, 300))  # Width, Height
        self.setMaximumSize(QSize(1000, 1000))  # Width, Height

    def __init__(self):
        super().__init__()
        self.setSizeOfWindow()
        self.setWindowTitle("Sign In")

        # Create the main widget and layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        # Create the username label and input field
        username_label = QLabel("Username:")
        self.username_input = QLineEdit()

        # Create the password label and input field
        password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        # Create the sign-in and register buttons
        sign_in_button = QPushButton("Sign In")
        register_button = QPushButton("Register")

        # Connect the sign-in and register button signals to slots
        sign_in_button.clicked.connect(self.sign_in)
        register_button.clicked.connect(self.register)

        # Add all the widgets to the layout
        main_layout.addWidget(username_label)
        main_layout.addWidget(self.username_input)
        main_layout.addWidget(password_label)
        main_layout.addWidget(self.password_input)
        main_layout.addWidget(sign_in_button)
        main_layout.addWidget(register_button)

        main_widget.setMaximumSize(QSize(300, 300))
        sign_in_button.setAlignment(Qt.AlignHCenter)
        # Set the main widget as the central widget of the window
        self.setCentralWidget(main_widget)
        start_color = Qt.white  # Replace with your desired start color
        end_color = Qt.blue  # Replace with your desired end color
        self.set_gradient_background(start_color, end_color)

    def sign_in(self):
        username = self.username_input.text()
        password = self.password_input.text()
        # Implement your sign-in logic here
        print(f"Signing in with username: {username} and password: {password}")

    def register(self):
        # Implement your registration logic here
        print("Opening registration window...")
    def set_gradient_background(widget, start_color, end_color):
        palette = widget.palette()
        gradient = QLinearGradient(0, 0, 0, widget.height())  # Create a linear gradient
        gradient.setColorAt(0, start_color)  # Set start color at position 0
        gradient.setColorAt(1, end_color)  # Set end color at position 1
        brush = QBrush(gradient)
        palette.setBrush(QPalette.Window, brush)  # Use Window role
        widget.setAutoFillBackground(True)
        widget.setPalette(palette)


app = QApplication(sys.argv)
font_id = QFontDatabase.addApplicationFont("sfPro/regular.OTF")
font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
app.setFont(font_family)
app.setStyleSheet("""
    /* Set the background color for the main window */
    QMainWindow {
        background-color: ;
    }

    /* Set the font family and size for the main window */
    QMainWindow QLabel, 
    QMainWindow QPlainTextEdit, 
    QMainWindow QComboBox,
    QMainWindow QLineEdit,
    QMainWindow QSpinBox,
    QMainWindow QSlider,
    QMainWindow QCheckBox,
    QMainWindow QRadioButton,
    QMainWindow QPushButton,
    QMainWindow QToolButton,
    QMainWindow QTabWidget,
    QMainWindow QMenuBar,
    QMainWindow QMenu,
    QMainWindow QAction,
    QMainWindow QStatusBar {
        font-size: 18px;
        text-align: right;
        border: 1px solid transparent;
    }
    
    QMainWindow QLabel{
        width: 1px;
    }

    /* Set the background color for various widgets */
    QMainWindow QTabWidget::pane {
        background-color: #ffffff;
    }

    QMainWindow QTabBar::tab {
        background-color: #e0e0e0;
    }

    QMainWindow QTabBar::tab:selected {
        background-color: #ffffff;
    }

    QMainWindow QMenuBar::item {
        background-color: #e0e0e0;
    }

    QMainWindow QMenuBar::item:selected {
        background-color: #ffffff;
    }

    /* Set the color for various widgets */
    QMainWindow QTabBar::tab,
    QMainWindow QCheckBox,
    QMainWindow QRadioButton,
    QMainWindow QLabel {
        color: #333333;
    }
""")


# Create window as an instance of Qt Widget
# window = QWidget()
mainWindow = SignInWindow()
mainWindow.show()               # window is hidden by default

# Start event loop
app.exec()

print("Hello widgets")


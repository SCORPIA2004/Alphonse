from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPainter, QColor, QBrush, QPen
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class CountdownProgressBar(QWidget):
    def __init__(self):
        super().__init__()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        # Set window properties
        self.setWindowTitle("Countdown Progress Bar")
        self.setFixedSize(200, 250)
        self.setAutoFillBackground(True)

        # Create layout
        layout = QVBoxLayout(self)
        self.setLayout(layout)

        # Create label and input field for minutes
        self.minutes_label = QLabel("Enter the number of minutes:")
        layout.addWidget(self.minutes_label)

        self.minutes_input = QLineEdit()
        self.minutes_input.setStyleSheet("color: white;")
        layout.addWidget(self.minutes_input)

        # Create start button
        self.start_button = QPushButton("Start")
        self.start_button.setStyleSheet("color: white;")
        self.start_button.clicked.connect(self.start_countdown)
        layout.addWidget(self.start_button)

        # Initialize minutes and seconds remaining
        self.minutes = 0
        self.seconds_remaining = 0

    def start_countdown(self):
        minutes_text = self.minutes_input.text()
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

        if self.seconds_remaining == 0:
            self.timer.stop()
            self.minutes_input.setEnabled(True)
            self.start_button.setEnabled(True)

    def paintEvent(self, event):
        painter = QPainter(self)

        # Calculate the progress percentage
        if self.minutes != 0:
            total_seconds = self.minutes * 60
            progress = (total_seconds - self.seconds_remaining) / total_seconds

        # Set colors
        bg_color = QColor(0, 0, 0)  # Black background
        ellipse_color = QColor(255, 0, 0)  # Red ellipse
        pie_color = QColor(255, 255, 150)  # Subtle yellow pie

        # Draw the background
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(bg_color))
        painter.drawRect(self.rect())

        # Draw the ellipse
        ellipse_pen = QPen(ellipse_color)
        ellipse_pen.setWidth(2)  # Set the width of the ellipse border
        painter.setPen(QColor(255, 255, 150))
        painter.setBrush(Qt.NoBrush)  # No brush for empty center
        painter.drawEllipse(10, 10, 90, 90)

        # Draw the progress pie
        painter.setBrush(QBrush(pie_color))
        painter.drawPie(10, 10, 90, 90, -90 * 16, -progress * 360 * 16)

app = QApplication([])

# Create the countdown progress bar window
window = CountdownProgressBar()

# Set window position and background color
window.move(1757, 0)
window.setFixedSize(105,105)

window.setStyleSheet("background-color: black;")

window.show()

app.exec()

from colorsys import hsv_to_rgb

from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget, QDial,
)
from PySide6.QtCore import Qt, QSize
from layout_colorwidget_hex import Color
import sys
import math

class MainWindow(QMainWindow):
    def setSizeOfWindow(self):
        screen = app.primaryScreen()
        screenGeometry = screen.geometry()

        width = screenGeometry.width() / 4
        height = screenGeometry.height() / 4
        self.setFixedSize(QSize(width, height))          # Width, Height

        # self.setFixedSize(QSize(960, 540))          # Width, Height
        self.setMinimumSize(QSize(300, 300))          # Width, Height
        self.setMaximumSize(QSize(1000, 1000))        # Width, Height

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rainbow fidget spinner")
        self.setSizeOfWindow()

        # create layouts. pageLayout: main layout, buttonLayout: layout for buttons
        pagelayout = QVBoxLayout()
        buttonLayout = QHBoxLayout()
        self.stacklayout = QStackedLayout()

        # set the layout
        pagelayout.addLayout(buttonLayout)
        pagelayout.addLayout(self.stacklayout)

        rainbowDial = QDial()
        rainbowDial.setRange(1, 200)
        rainbowDial.setSingleStep(1)
        rainbowDial.setNotchesVisible(True)
        rainbowDial.valueChanged.connect(self.value_changed)
        rainbowDial.sliderMoved.connect(self.slider_position)
        rainbowDial.sliderPressed.connect(self.slider_pressed)
        rainbowDial.sliderReleased.connect(self.slider_released)

        # add widgets
        pagelayout.addWidget(rainbowDial)
        import math

        for i in range(200):
            # Calculate the color values for the current position in the spectrum
            ratio = i / 200.0
            hue = ratio * 0.8  # Adjust this value to change the range of colors
            rgb = hsv_to_rgb(hue, 1, 1)  # Convert HSV to RGB values

            r = int(rgb[0] * 255)
            g = int(rgb[1] * 255)
            b = int(rgb[2] * 255)

            self.stacklayout.addWidget(Color(r, g, b, 127))

        # set the layout
        container = QWidget()
        container.setLayout(pagelayout)
        self.setCentralWidget(container)

    def value_changed(self, i):
        self.stacklayout.setCurrentIndex(i)

    def slider_position(self, p):
        print(p)

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

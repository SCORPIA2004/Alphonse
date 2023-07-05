from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QWidget
class Color(QWidget):
  def __init__(self, r, g, b, transparency):
      super().__init__()
      self.setAutoFillBackground(True)
      palette = self.palette()
      palette.setColor(QPalette.Window, QColor(r, g, b, transparency))
      self.setPalette(palette)
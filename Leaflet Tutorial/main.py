import io
import sys
import os
from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget


def main():
    app = QApplication(sys.argv)

    # Create the main window widget
    window = QWidget()
    window.setWindowTitle("Leaflet Map in PySide6 QWebEngineView")
    window.resize(940, 620)

    # Create a layout to hold the QWebEngineView widget
    layout = QVBoxLayout(window)

    # Create a QWebEngineView widget
    web_view = QWebEngineView()

    # Load the HTML template into the QWebEngineView widget
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(current_dir)

    html_path = os.path.join(current_dir, "map.html")
    with open(html_path, "r") as f:
        HTML_TEMPLATE = f.read()

    # Rest of the code remains unchanged
    web_view.setHtml(HTML_TEMPLATE)

    # Add the QWebEngineView widget to the layout
    layout.addWidget(web_view)

    # Show the main window
    window.show()

    # Start the application event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

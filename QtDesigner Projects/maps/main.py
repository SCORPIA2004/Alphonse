import sys, io, folium
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Folium Map")
        self.windowWidth, self.windowHeight = 1600, 900
        self.setMinimumSize(self.windowWidth, self.windowHeight)

        # layout = QVBoxLayout()
        # self.setLayout(layout)

        central_widget = QWidget()  # Create a central widget
        self.setCentralWidget(central_widget)  # Set the central widget for QMainWindow

        layout = QVBoxLayout(central_widget)  # Use the central widget for the layout

        coordinate = (39.865506432608136, 32.74609830979015)

        m = folium.Map(
            title="Bilka hill",
            zoom_start=13,
            location=coordinate
        )

        m = folium.Marker(
            location=coordinate,
            popup="Bilkent Hill",
            tooltip="Bilkent Hill",
            icon=folium.Icon(color="green", icon="leaf")
        ).add_to(m)
        forLatLng = folium.ClickForLatLng().add_to(m)
        # m = folium.ClickForMarker().add_to(m)
        marker = folium.ClickForMarker("<b>Lat:</b> ${lat}<br /><b>Lon:</b> ${lng}")
        m.add_child(marker)
        # save map data
        data = io.BytesIO()
        m.save(data, close_file=False)


        mapWebView = QWebEngineView()
        mapWebView.setHtml(data.getvalue().decode())

        layout.addWidget(mapWebView)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

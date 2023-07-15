from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication, QMainWindow


class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Map Viewer")
        self.map_view = QWebEngineView()
        self.setCentralWidget(self.map_view)

    def load_map(self):
        # Set your Google Maps API key here
        api_key = "YOUR_API_KEY"
        # Construct the HTML code to embed the map
        html = """
        <!DOCTYPE html>
        <html>
          <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <script src="https://maps.googleapis.com/maps/api/js?key={}&callback=initMap"></script>
            <style>
              #map {{
                height: 100%;
              }}
            </style>
          </head>
          <body>
            <div id="map"></div>
            <script>
              function initMap() {{
                var map = new google.maps.Map(document.getElementById("map"), {{
                  zoom: 12,
                  center: {{ lat: 37.7749, lng: -122.4194 }}  // Set the initial center position
                }});
              }}
            </script>
          </body>
        </html>
        """.format(api_key)
        # Load the HTML content into the QWebEngineView widget
        self.map_view.setHtml(html)



if __name__ == "__main__":
    app = QApplication([])
    window = MapWindow()
    window.load_map()
    window.show()
    app.exec()

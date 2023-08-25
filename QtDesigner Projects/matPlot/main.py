import sys
import matplotlib
matplotlib.use('QtAgg')
from PySide6 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        # fig = Figure()
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create the maptlotlib FigureCanvas object, which defines a single set of axes as self.axes.
        sc = MplCanvas(self, width=5, height=4, dpi=100)

        # Get data from test.csv
        with open('test.csv', 'r') as f:
            csvReader = f.read()
            data = []
            x = []
            y = []
            count = 0
            for row in csvReader.split('\n'):
                # print(row)
                data.append(row.split(','))
                if count != 0:
                    try:
                        x.append(count)
                        # x.append(data[count][0])
                        y.append(float(data[count][2]))
                    except:
                        print('Error')
                count += 1
                if count == 330:
                    print("debug")


        sc.axes.plot(x, y)

        # sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(sc, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        matPlot = QtWidgets.QWidget()
        matPlot.setLayout(layout)
        self.setCentralWidget(matPlot)

        self.show()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec()
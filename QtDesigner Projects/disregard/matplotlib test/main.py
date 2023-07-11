import sys
import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import Tk, Button, filedialog, Label, Entry
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a layout
        layout = QVBoxLayout()

        # Create a spacer to push the button to the center
        spacer = QWidget()
        spacer.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        layout.addWidget(spacer)

        fileUploadingLayout = QHBoxLayout()

        # create display for filename
        self.filenameDisplay = QLineEdit("No file selected")
        # self.filenameDisplay.setFixedWidth(100)
        fileUploadingLayout.addWidget(self.filenameDisplay)


        # Create the button
        uploadFile = QPushButton("Upload File")
        uploadFile.clicked.connect(self.getFile)
        uploadFile.setFixedWidth(100)
        fileUploadingLayout.addWidget(uploadFile)

        layout.addLayout(fileUploadingLayout)

        # second layout
        tOptimalLayout = QHBoxLayout()


        # Create t_optimal value
        self.var = QLabel("")
        layout.addWidget(self.var)
        tOptimalLayout.addWidget(self.var)

        # Ask for inout for t_optimal_entry
        self.t_optimal_entry = QLineEdit()
        self.t_optimal_entry.setMaxLength(10)
        self.t_optimal_entry.setPlaceholderText("Enter your t_optimal_entry")
        tOptimalLayout.addWidget(self.t_optimal_entry)
        layout.addLayout(tOptimalLayout)


        # Create a Matplotlib figure and canvas
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)

        # Add the canvas to the layout
        layout.addWidget(self.canvas)

        # Set the layout on a central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Plot your data
        self.ax = self.fig.add_subplot(111)
        self.ax.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
        # sets graph title to Hysteris curve + date and time
        # ax.set_title("Hystersis curve %s", time.localtime())

    def closeEvent(self, event):
        # Clean up resources before closing the application
        plt.close('all')
        event.accept()

    def getFile(self):
        print("uploading file")
        filename, selectedFilter = QFileDialog.getOpenFileNames(self)
        self.filenameDisplay.setText(filename[0])
        self.plot_graph(file_path=filename[0])

    def plot_graph(self, file_path=None, custom_t_optimal=None):
        global t_optimal, original_t_optimal

        if file_path is None and custom_t_optimal is None:
            print("No file selected.")
            return

        # Read the file
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path, encoding="ISO-8859-1")
        elif file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        else:
            print("Unsupported file format.")
            return

        # Filter and clean the data
        df = df.dropna(subset=['H GaussMeter (Oe)', 'Mx (emu)']).reset_index(drop=True)

        # Convert the data to a numpy array
        H = df['H GaussMeter (Oe)'].to_numpy()
        Mx = df['Mx (emu)'].to_numpy()

        offset = Mx[0]

        # Track the increasing and decreasing direction of H
        direction = np.sign(np.diff(H))
        turning_points = np.where(np.diff(direction))[0]

        # Calculate Mxnew values for each "t" value and compute the y-difference at the edges
        t_values = np.linspace(1e-15, 1e-3, 100000)

        edge_diffs = []

        for t in t_values:
            Mxnew = (Mx - H * t) - offset
            # Compute the y-difference at the edges
            edge_diff = abs(np.diff(Mxnew)[turning_points[-1]] - np.diff(Mxnew)[turning_points[-2]])
            edge_diffs.append(edge_diff)

        # Find the "t" value that minimizes the y-difference at the edges
        min_index = np.argmin(edge_diffs)
        t_optimal = t_values[min_index]
        if t_optimal < 1e-07:
            t_optimal /= 30

        if custom_t_optimal is None:
            # Calculate Mxnew values with the optimal "t" value
            Mxnew = (Mx - H * t_optimal) - offset
        else:
            # Calculate Mxnew values with the custom "t" value
            Mxnew_custom = (Mx - H * custom_t_optimal) - offset

        # Create the plot
        self.ax.plot(H, Mx, color='orange', label='Original', marker='o', markersize=5, linestyle='-', linewidth=1)

        if custom_t_optimal is not None:
            # Plot the custom Mxnew values with lines
            self.ax.plot(H, Mxnew_custom, color='black', label=f'Optimized (t={custom_t_optimal})', marker='o', markersize=5,
                    linestyle='-', linewidth=1)

            original_t_optimal = t_optimal  # Store the original "t" value
            t_optimal = custom_t_optimal  # Set the current "t" value as the custom "t" value
        else:
            # Plot the optimized data with lines
            self.ax.plot(H, Mxnew, color='black', label=f'Optimized (t={t_optimal})', marker='o', markersize=5,
                    linestyle='-',
                    linewidth=1)

            original_t_optimal = t_optimal  # Store the original "t" value

        self.ax.grid(True, linestyle='--', linewidth=0.5, color='gray')

        self.canvas.draw()

        print(f"Optimal t value: {t_optimal}")
        self.var.setText(str(original_t_optimal))  # Update the label text
        return t_optimal, original_t_optimal

    def submit_t_optimal(self, event=None):
        custom_t_optimal_str = self.t_optimal_entry.get()
        if custom_t_optimal_str:
            custom_t_optimal = float(custom_t_optimal_str)
            self.clear_graph()
            self.plot_graph(file_path=self.file_name[0], custom_t_optimal=custom_t_optimal)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create the main window
    window = MainWindow()
    window.show()

    # Start the event loop
    sys.exit(app.exec())

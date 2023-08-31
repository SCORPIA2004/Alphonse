from tkinter import Tk

import numpy as np
import matplotlib.pyplot as plt
from kneed import KneeLocator
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from scipy.signal import savgol_filter
import csv
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def movingAverageSmoothing(x, y, type):
    # Generate sample noisy data

    # Smoothing parameters
    window_size_ma = 7  # Moving average window size
    window_size_sg = 7  # Savitzky-Golay window size
    poly_order_sg = 3   # Savitzky-Golay polynomial order

    x_noisy = np.array(x)
    y_noisy = np.array(y)

    # Apply moving average filter
    if type == 1:
        smoothed_ma = np.convolve(y_noisy, np.ones(window_size_ma)/window_size_ma, mode='same')
    else:
        smoothed_ma = np.convolve(x_noisy, np.ones(window_size_ma)/window_size_ma, mode='same')


    # Apply Savitzky-Golay filter
    # y_smoothed_sg = savgol_filter(y_noisy, window_size_sg, poly_order_sg)
    # plotGraph(x, gradient, "Gradient")
    return smoothed_ma

def computeArea(pos):
    x, y = (zip(*pos))
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))

def areaEnclosed(xAxis, yAxis):
    # Plot the results
    x = np.array(xAxis)
    y = np.array(yAxis)

    plt.figure(figsize=(10, 6))
    # plt.plot(x, y, label='Hysteresis', linewidth=2)
    polygon = plt.fill(x, y, 'b', alpha=0.3)
    # area = computeArea(polygon[0].xy)
    pos = polygon[0].xy
    x, y = (zip(*pos))
    area = 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


    # print("Area: ", area)
    return area

def plotGraph(x, y, title, saturationPoint=0):
    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='Hysteresis', linewidth=2)
    # plot a vertical line at the knee
    if saturationPoint != 0:
        plt.vlines(saturationPoint, plt.ylim()[0], plt.ylim()[1], linestyles='dashed', colors='r', label='Saturation point')

    # index = np.where(x == x.max())[0].item()
    # polygon = plt.fill(x[index:], y[index:], 'b', alpha=0.3)
    polygon = plt.fill(x, y, 'b', alpha=0.3)
    computeArea(polygon[0].xy)
    # areaEnclosed(x, y, polygon)

    # plt.xlim(-30, 30)
    # plt.ylim(-2, 2)

    # make x axis line
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')


    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

def calculate_gradients(x, y):
    # Convert input arrays to numpy arrays
    x = np.array(x)
    y = np.array(y)

    # Calculate the differences between consecutive x and y values
    dx = np.diff(x)
    dy = np.diff(y)


    # Calculate gradients using the differences
    # gradients = dy / dx
    valid_indices = dx != 0
    gradients = np.zeros_like(dx)
    gradients[valid_indices] = dy[valid_indices] / dx[valid_indices]
    gradients[~valid_indices] = 0

    return gradients

def largest(arr, n):
    # Initialize maximum element
    max = arr[0]

    # Traverse array elements from second
    # and compare every element with
    # current max
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max

def saturationField(xAxis, yAxis):

    #### OLD CODE working with offset = kneedle.knee + kneedle.knee / 2
    xAxisArr = np.array(xAxis)
    yAxisArr = np.array(yAxis)
    # kneedle = KneeLocator(xAxisArr, yAxisArr, S=1.0, curve="concave", direction="increasing")
    # saturationPointX = kneedle.knee + kneedle.knee / 2
    # # saturationPointX = kneedle.knee + largest(xAxisArr, xAxisArr.size) / 3
    #
    # gradArr = calculate_gradients(xAxisArr, yAxisArr)
    # plotGraph(xAxisArr, yAxisArr,"Hysteresis curve", saturationPoint=saturationPointX)
    # # plotGraph(xAxis[:-1], gradArr,"Gradient", saturationPoint=saturationPoint)
    # print(round(saturationPointX, 3))
    # # find x value closest to saturationPointX
    # saturationPointX = min(xAxisArr, key=lambda x:abs(x-saturationPointX))
    # # print("Closest x:  ", saturationPointX)
    # # find index of saturationPointX
    saturationPointX = saturationPoint(xAxis, yAxis)
    index = np.where(xAxisArr == saturationPointX)[0].item() + 1
    # print("Index: ", index)
    saturationPointY = yAxisArr[index]
    print("Saturation field: ", saturationPointY)
    return saturationPointY

def saturationPoint(xAxis, yAxis):

    xAxisArr = np.array(xAxis)
    yAxisArr = np.array(yAxis)

    kneedle = KneeLocator(xAxisArr, yAxisArr, S=1.0, curve="concave", direction="increasing")
    saturationPointX = kneedle.knee + largest(xAxisArr, xAxisArr.size) / 3

    # plotGraph(xAxisArr, yAxisArr,"Hysteresis curve", saturationPoint=saturationPoint)
    gradArr = calculate_gradients(xAxisArr, yAxisArr)
    # plotGraph(xAxis[:-1], gradArr,"Gradient", saturationPoint=saturationPoint)
    # print(round(saturationPointX, 3))
    # find x value closest to saturationPointX
    saturationPointX = min(xAxisArr, key=lambda x:abs(x-saturationPointX))
    # print("Closest x:  ", saturationPointX)
    # find index of saturationPointX
    index = np.where(xAxisArr == saturationPointX)[0].item() + 1
    # print("Index: ", index)


    return saturationPointX

def slopeAtCoerciveField(xAxis, yAxis):
    xAxisArr = np.array(xAxis)
    yAxisArr = np.array(yAxis)

    gradientArr = calculate_gradients(xAxisArr, yAxisArr)
    maxGradient = gradientArr.max()
    print("slope at coercive field: ", maxGradient)
    return maxGradient

def sfd(xAxis, yAxis):
    xAxisArr = np.array(xAxis)
    yAxisArr = np.array(yAxis)
    gradArr = calculate_gradients(xAxisArr, yAxisArr)

    # max of gradArr
    maxGrad = gradArr.max()
    # print("maxGrad: ", maxGrad)
    halfGrad = maxGrad / 2

    # find grad value closest to halfGrad
    halfGrad = min(gradArr, key=lambda x:abs(x-halfGrad))
    # print("Closest gradient to the half:  ", halfGrad)

    # find index of halfGrad
    indexOfHalfGrad = np.where(gradArr == halfGrad)[0].item() + 1
    # print("Index: ", index)
    # print("x value: ", xAxisArr[index])

    widthOfHalfMaxGradient = indexOfHalfGrad * 2

    # find x value where curve intersects x axis
    # find x value where y value is closest to 0
    indexHc = (np.abs(yAxisArr - 0)).argmin()
    hc = xAxisArr[indexHc]
    # print("Index: ", indexHc)
    # print("Closest y to 0:  ", hc)
    sfdValue = widthOfHalfMaxGradient / hc
    print("SFD: ", sfdValue)
    return sfdValue

def initialSlope(xAxis, yAxis):
    xAxisArr = np.array(xAxis)
    yAxisArr = np.array(yAxis)
    gradArr = calculate_gradients(xAxisArr, yAxisArr)

    # find index when xAxisArr element is closest to 0
    index = (np.abs(xAxisArr - 0)).argmin() + 1
    print("Index: ", index)
    initialSlopeValue = gradArr[index]
    print("Initial slope is ", initialSlopeValue)
    return initialSlopeValue

def rigidField(xAxis, yAxis):
    xAxisArr = np.array(xAxis)
    yAxisArr = np.array(yAxis)
    # xAxisArrOld = np.array(xAxis)
    # yAxisArrOld = np.array(yAxis)
    #
    # xAxisArr = movingAverageSmoothing(xAxisArrOld, yAxisArrOld, 0)
    # yAxisArr = movingAverageSmoothing(xAxisArrOld, yAxisArrOld, 1)

    gradArr = calculate_gradients(xAxisArr, yAxisArr)

    # find index when xAxisArr element is closest to 0
    index = (np.abs(xAxisArr - 0)).argmin()
    print("Index: ", index)
    y2 = yAxisArr[index]
    y1 = yAxisArr[index + 1]
    print("Point y2: ", y2, "Point y1: ", y1)
    x2 = xAxisArr[index]
    x1 = xAxisArr[index + 1]
    print("Point x2: ", x2, "Point x1: ", x1)
    gradient = (y2 - y1) / (x2 - x1)
    print("Gradient: ", gradient)
    c = y2 - gradient * x2
    print("c: ", c)
    print("Remanent magnetization: ", c)

    return c
    # xAxisArr = np.array(xAxis)
    # yAxisArr = np.array(yAxis)
    # gradArr = calculate_gradients(xAxisArr, yAxisArr)
    #
    # # find index when xAxisArr element is closest to 0
    # index = (np.abs(xAxisArr - 0)).argmin() + 1
    # print("Index: ", index)
    # rf = xAxisArr[index]
    # print("Rigid field: ", rf)
    # return rf

def coerciveField(xAxis, yAxis):
    xAxisArr = np.array(xAxis)
    yAxisArr = np.array(yAxis)

    # find index when xAxisArr element is closest to 0
    index = (np.abs(yAxisArr - 0)).argmin()
    print("Index: ", index)
    coerciveField = xAxisArr[index]
    print("Coercive field: ", coerciveField)
    return coerciveField

def remMag(xAxis, yAxis):
    xAxisArr = np.array(xAxis)
    yAxisArr = np.array(yAxis)
    # xAxisArrOld = np.array(xAxis)
    # yAxisArrOld = np.array(yAxis)
    #
    # xAxisArr = movingAverageSmoothing(xAxisArrOld, yAxisArrOld, 0)
    # yAxisArr = movingAverageSmoothing(xAxisArrOld, yAxisArrOld, 1)



    gradArr = calculate_gradients(xAxisArr, yAxisArr)

    # find index when xAxisArr element is closest to 0
    index = (np.abs(xAxisArr - 0)).argmin()
    print("Index: ", index)
    y2 = yAxisArr[index]
    y1 = yAxisArr[index + 1]
    print("Point y2: ", y2, "Point y1: ", y1)
    x2 = xAxisArr[index]
    x1 = xAxisArr[index + 1]
    print("Point x2: ", x2, "Point x1: ", x1)
    gradient = (y2 - y1) / (x2 - x1)
    print("Gradient: ", gradient)
    c = y2 - gradient * x2
    print("c: ", c)


    # print("Remanent magnetization: ", rf)
    return c


class PlotterApp:
    def __init__(self, root, saturationPointX=0, saturationPointY=0, nucleationField=0, remMag=0, coerciveField=0):
        self.saturationPointX = saturationPointX
        self.saturationPointY = saturationPointY
        self.nucleationField = nucleationField
        self.coerciveField = coerciveField
        self.remMag = remMag
        self.root = root
        self.root.title("Tkinter Plotter")

        self.xdata = []
        self.ydata = []

        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.plot = self.figure.add_subplot(1, 1, 1)

        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.toolbar = NavigationToolbar2Tk(self.canvas, root)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.plot_button = tk.Button(root, text="Plot", command=self.plot_graph)
        self.plot_button.pack(side=tk.BOTTOM)




    def plot_graph(self, saturationPoint=0):
        self.plot.clear()
        self.plot.plot(self.xdata, self.ydata, marker='.', linewidth=1, markersize=1)

        self.plot.set_xlabel("X Axis")
        self.plot.set_ylabel("Y Axis")
        self.plot.set_title("Plot")
        self.plot.grid(True)
        self.plot.axhline(y=0, color='k')
        self.plot.axvline(x=0, color='k')
        # self.plot.axvline(x=self.saturationPointX, color='r', linestyle='dashed', label='Ms')
        # self.plot.axhline(y=self.saturationPointY, color='g', linestyle='dashed', label='Hs')
        self.plot.scatter(self.saturationPointX, self.saturationPointY, color='r', marker='^', label='Ms')
        # self.plot.scatter(0, self.remMag, color='g', marker='^', label='Mr')
        # self.plot.scatter(self.coerciveField, 0, color='b', marker='^', label='Hc')
        # self.plot.axvline(x=self.nucleationField, color='k', linestyle='dashed', label='Hn')


        self.plot.legend()

        self.canvas.draw()

    def set_data(self, xdata, ydata):
        self.xdata = xdata
        self.ydata = ydata
def main():

    # Initialize empty arrays to store the data
    column1 = []
    column2 = []

    # Specify the path to your CSV file
    csv_file_path = 'Ni-CYL - 1.csv'  # Update with the actual file path
    # csv_file_path = 'Ni - CYL - 2.csv'  # Update with the actual file path
    # csv_file_path = 'sample1.csv'  # Update with the actual file path
    # csv_file_path = 'sample3.csv'  # Update with the actual file path
    # csv_file_path = 'sample4.csv'  # Update with the actual file path

    # Open and read the CSV file
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # waste first row
        next(csv_reader)

        # Iterate through each row in the CSV file
        for row in csv_reader:
            # Assuming the first two columns contain the data you want to store
            if len(row) >= 2:
                column1.append(float(row[0]))  # Convert to float if necessary
                column2.append(float(row[1]))  # Convert to float if necessary

    # Now smooth the curve using moving average
    xAxis = np.array(column1)
    yAxis = np.array(column2)



    gradArr = calculate_gradients(xAxis, yAxis)
    # remove the last value from xAxis and yAxis
    # xAxis = xAxis[:-1]
    # yAxis = yAxis[:-1]

    saturationPointValX = saturationPoint(xAxis, yAxis)
    saturationPointValY = saturationField(xAxis, yAxis)
    nucleationField = max(xAxis)
    print("Nucleation field: ", nucleationField)
    root = Tk()
    app = PlotterApp(root, saturationPointX=saturationPointValX, saturationPointY=saturationPointValY, nucleationField=nucleationField)
    app.set_data(xAxis, yAxis)

    print("Saturation point: ", saturationPointValX, saturationPointValY)
    # plotGraph(xAxis, yAxis,"Hysteresis curve", saturationPoint=saturationPointVal)
    # plot the gradient
    # plotGraph(xAxis[:-1], gradArr,"Gradient", saturationPoint=saturationPointVal)

    slopeAtCoerciveField(xAxis, yAxis)
    saturationPoint(xAxis, yAxis)
    saturationField(xAxis, yAxis)
    sfd(xAxis, yAxis)
    initialSlope(xAxis, yAxis)
    remMagVal = remMag(xAxis, yAxis)
    rigidField(xAxis, yAxis)
    coercive = coerciveField(xAxis, yAxis)
    root.mainloop()

    root = Tk()
    app = PlotterApp(root, saturationPointX=saturationPointValX, saturationPointY=saturationPointValY, nucleationField=nucleationField, remMag=remMagVal, coerciveField=coercive)
    app.set_data(xAxis, yAxis)

if __name__ == '__main__':
        main()
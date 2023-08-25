import numpy as np
import matplotlib.pyplot as plt
from kneed import KneeLocator
from scipy.signal import savgol_filter
import csv

def movingAverageSmoothing(x, y_noisy, gradient):
    # Generate sample noisy data

    # Smoothing parameters
    window_size_ma = 7  # Moving average window size
    window_size_sg = 7  # Savitzky-Golay window size
    poly_order_sg = 3   # Savitzky-Golay polynomial order

    # Apply moving average filter
    y_smoothed_ma = np.convolve(y_noisy, np.ones(window_size_ma)/window_size_ma, mode='same')

    # Apply Savitzky-Golay filter
    y_smoothed_sg = savgol_filter(y_noisy, window_size_sg, poly_order_sg)
    # plotGraph(x, gradient, "Gradient")



def plotGraph(x, y, title, knee=0):
    # Plot the results
    plt.figure(figsize=(10, 6))
    # plt.plot(x, y_noisy, label='Noisy Data', alpha=0.5, marker='o')
    # plt.plot(x, y_smoothed_ma, label='Smoothed (Moving Average)', linewidth=2)
    # plt.plot(x, y_smoothed_sg, label='Smoothed (Savitzky-Golay)', linewidth=2)
    plt.plot(x, y, label='Gradient', linewidth=2)
    # plot a vertical line at the knee
    plt.vlines(knee, plt.ylim()[0], plt.ylim()[1], linestyles='dashed')

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



def main():
    # Initialize empty arrays to store the data
    column1 = []
    column2 = []

    # Specify the path to your CSV file
    csv_file_path = 'Ni-CYL - 1.csv'  # Update with the actual file path
    # csv_file_path = 'Ni - CYL - 2.csv'  # Update with the actual file path
    # csv_file_path = 'sample1.csv'  # Update with the actual file path
    # csv_file_path = 'sample3.csv'  # Update with the actual file path

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
    xAxis = xAxis[:-1]
    yAxis = yAxis[:-1]

    # plotGraph(xAxis, gradArr, "Gradient kneed")
    print(gradArr.size)

    kneedle = KneeLocator(xAxis, yAxis, S=1.0, curve="concave", direction="increasing")
    kneedle.knee = kneedle.knee + largest(xAxis, xAxis.size) / 3
    plotGraph(xAxis, yAxis,"Hysteresis kneed", knee=kneedle.knee)
    # plotGraph(xAxis, gradArr,"Gradient", knee=kneedle.knee)
    print(round(kneedle.knee, 3))


if __name__ == '__main__':
    main()
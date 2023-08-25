import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import csv

def saturation(y_noisy):
    # Generate sample noisy data
    np.random.seed(0)
    x = np.linspace(0, 10, 100)
    y_noisy = np.sin(x) + np.random.normal(0, 0.2, len(x))

    # Smoothing parameters
    window_size_ma = 7  # Moving average window size
    window_size_sg = 7  # Savitzky-Golay window size
    poly_order_sg = 3   # Savitzky-Golay polynomial order

    # Apply moving average filter
    y_smoothed_ma = np.convolve(y_noisy, np.ones(window_size_ma)/window_size_ma, mode='same')

    # Apply Savitzky-Golay filter
    y_smoothed_sg = savgol_filter(y_noisy, window_size_sg, poly_order_sg)

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(x, y_noisy, label='Noisy Data', alpha=0.5, marker='o')
    plt.plot(x, y_smoothed_ma, label='Smoothed (Moving Average)', linewidth=2)
    plt.plot(x, y_smoothed_sg, label='Smoothed (Savitzky-Golay)', linewidth=2)

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Hysteresis Curve with Smoothing')
    plt.legend()
    plt.grid(True)

    plt.show()




# Initialize empty arrays to store the data
column1 = []
column2 = []

# Specify the path to your CSV file
csv_file_path = 'Ni-CYL - 1.csv'  # Update with the actual file path

# Open and read the CSV file
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Assuming the first two columns contain the data you want to store
        if len(row) >= 2:
            column1.append(float(row[0]))  # Convert to float if necessary
            column2.append(float(row[1]))  # Convert to float if necessary
            print(float(row[0]), float(row[1]))

# Now, column1 and column2 contain the data from the first two columns of the CSV file

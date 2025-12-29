"""
This code will:
Read average weather data from file and store values in lists.
Create a line graph for average high and low temperatures.
Find and print highest and lowest average temperatures.
Read extreme temperature and snowfall data from file.
Create a bar graph for record high and low temperatures.
Create a pie chart for snowfall distribution.
Calculate temperature ranges and display them in a line graph.
Print summary statistics for each graph.
"""

import os
import matplotlib.pyplot as plt

# File paths for CSV data
PATH_WEATHER = os.path.join("docs", "weather_data_flatbush.csv")
PATH_EXTREMES = os.path.join("docs", "flatbush_extremes.csv")

# Lists to store monthly weather data
months = []
high_temps = []
low_temps = []
rains = []

# Lists to store extreme/record weather data
extreme_high_temps = []
extreme_low_temps = []
snows = []

# Color palette for graphs
colors = ("#cdb4db", "#ffc8dd", "#a2d2ff", "#f7e1d7", "#caffbf", "#ffd6a5")


def weather_data():
    """
    This function reads the average weather data file.
    It stores monthly temperatures and rainfall into lists.
    The data is used for the line chart.
    """
    with open(PATH_WEATHER, "r") as f:
        header = f.readline()  # Skip header line

        for line in f:
            line = line.strip()
            line = line.split(",")

            # Assign values from CSV
            month = line[0]
            high_temp = int(line[1])
            low_temp = int(line[2])
            rain = float(line[3])

            # Store values in lists
            months.append(month)
            high_temps.append(high_temp)
            low_temps.append(low_temp)
            rains.append(rain)


def line_chart():
    """
    This function creates a line graph of average temperatures.
    It compares monthly high and low temperatures.
    The graph shows seasonal temperature changes.
    """
    x_coords = list(range(len(months)))
    y_coords = [0, 10, 20, 30, 40, 50, 60, 70, 80]

    plt.plot(x_coords, high_temps, label="Avg High Temp", color=colors[0], marker='o')
    plt.plot(x_coords, low_temps, label="Avg Low Temp", color=colors[2], marker='o')

    plt.title("Average High and Low Temperatures by Month")
    plt.xlabel("Months")
    plt.ylabel("Temperature")

    plt.xticks(x_coords, months)
    plt.yticks(y_coords)
    plt.grid(True)

    plt.show()


def extremes_data():
    """
    This function reads the extreme weather data file.
    It stores record high, record low, and snowfall values.
    The data is used for the bar and pie charts.
    """
    with open(PATH_EXTREMES, "r") as f:
        header = f.readline()

        for line in f:
            line = line.strip()
            line = line.split(",")

            extreme_high_temp = int(line[1])
            extreme_low_temp = int(line[2])
            snow = float(line[3])

            extreme_high_temps.append(extreme_high_temp)
            extreme_low_temps.append(extreme_low_temp)
            snows.append(snow)


def bar_chart():
    """
    This function creates a bar graph of extreme temperatures.
    It compares record high and record low temperatures.
    The bars show how extreme temperatures vary by month.
    """
    x_coords = list(range(len(months)))
    bar_width = 0.3

    plt.bar([x + bar_width/2 for x in x_coords],
            extreme_high_temps, width=bar_width, label="High", color=colors[3])
    plt.bar([x - bar_width/2 for x in x_coords],
            extreme_low_temps, width=bar_width, label="Low", color=colors[1])

    plt.title("Record High and Low Temperatures by Month")
    plt.xlabel("Months")
    plt.ylabel("Temperature")

    plt.xticks(x_coords, months)
    plt.grid(True)
    plt.show()


def pie_chart():
    """
    This function creates a pie chart of snowfall.
    It shows how snowfall is distributed by month.
    Each slice represents a month.
    """
    plt.pie(snows, labels=months, colors=colors, autopct="%1.2f%%")

    plt.title("Snowfall Distribution by Month")
    plt.axis("equal")
    plt.show()

def largest_temp_range_chart():
    """
    This function calculates temperature ranges for each month.
    It creates a line graph using those ranges.
    The graph shows how much temperatures can vary.
    """
    ranges = []

    # Calculate range for each month
    for i in range(len(months)):
        temp_range = extreme_high_temps[i] - extreme_low_temps[i]
        ranges.append(temp_range)

    x_coords = list(range(len(months)))
    y_coords = [0, 10, 20, 30, 40, 50, 60, 70, 80]

    plt.plot(x_coords, ranges, label="Ranges", color=colors[5], marker='o')

    plt.title("Temperature Ranges by Month")
    plt.xlabel("Months")
    plt.ylabel("Temperature")

    plt.xticks(x_coords, months)
    plt.yticks(y_coords)
    plt.grid(True)

    plt.show()

    return ranges


def main():
    """
    This function runs the entire program.
    It calls all data and graph functions.
    It prints summary statistics for each graph.
    """
    weather_data()
    line_chart()

    # Graph 1 calculations
    max_high = max(high_temps)
    min_low = min(low_temps)

    max_month = months[high_temps.index(max_high)]
    min_month = months[low_temps.index(min_low)]

    print("--- GRAPH 1 ---")
    print(f"The month with the highest value is: {max_month} ({max_high})")
    print(f"The month with the lowest value is: {min_month} ({min_low})")
    print(f"The difference between highest and lowest is: {max_high - min_low}")

    extremes_data()
    bar_chart()

    # Graph 2 calculations
    max_extreme = max(extreme_high_temps)
    min_extreme = min(extreme_low_temps)

    max_month = months[extreme_high_temps.index(max_extreme)]
    min_month = months[extreme_low_temps.index(min_extreme)]

    print("--- GRAPH 2 ---")
    print(f"The month with the highest value is: {max_month} ({max_extreme})")
    print(f"The month with the lowest value is: {min_month} ({min_extreme})")
    print(f"The difference between highest and lowest is: {max_extreme - min_extreme}")

    pie_chart()

    # Graph 3 calculations
    max_snow = max(snows)
    min_snow = min(snows)

    max_month = months[snows.index(max_snow)]
    min_month = months[snows.index(min_snow)]

    print("--- GRAPH 3 ---")
    print(f"The month with the highest value is: {max_month} ({max_snow})")
    print(f"The month with the lowest value is: {min_month} ({min_snow})")
    print(f"The total snowfall is: {sum(snows)}")

    largest_temp_range_chart()

    # Graph 4 calculations
    ranges = []
    for i in range(len(months)):
        ranges.append(extreme_high_temps[i] - extreme_low_temps[i])

    max_range = max(ranges)
    min_range = min(ranges)

    max_month = months[ranges.index(max_range)]
    min_month = months[ranges.index(min_range)]

    print("--- GRAPH 4 ---")
    print(f"The month with the highest value is: {max_month} ({max_range})")
    print(f"The month with the lowest value is: {min_month} ({min_range})")
    print(f"The average temperature range is: {sum(ranges) / len(ranges):.2f}")


if __name__ == "__main__":
    main()
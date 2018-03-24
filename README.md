# Power Parser
Python software for parsing, plotting, and analyzing power data from SCE, or any other power company that uses Green Button data formats. (https://www.energy.gov/data/green-button)

Power Parser can be used as a standalone application to generate interactive plots from provided usage data. Additionally, it can be used as a library to provide parsing functions for provided data in other python projects.

## Standalone Usage

Power Parser can easily parse Green Button csv data files and generate useful, interactive plots. Just execute the software and pass in the dataset you would like to plot.

Use provided data to generate sample plots:
```
python power_parser.py unit_tests/usage_data.csv
```

This will generate 6 different plots:
1. Time series plot of all data in CSV.
![Time Series](documentation/power_usage.png?raw=true "Title")
1. Box and Whisker plot of power usage for each day of the week.
![Time Series](documentation/day_of_week.png?raw=true "Title")
1. Time series plot of power usage per week.
![Time Series](documentation/weekly.png?raw=true "Title")
1. Box and Whisker plot of power usage per hour in the day.
![Time Series](documentation/per_hour.png?raw=true "Title")
1. Box and Whisker plot of power usage per hour in the day for weekdays only.
![Time Series](documentation/weekdays.png?raw=true "Title")
1. Box and Whisker plot of power usage per hour in the day for weekends only.
![Time Series](documentation/weekends.png?raw=true "Title")

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
1. Box and Whisker plot of power usage for each day of the week.
1. Time series plot of power usage per week.
1. Box and Whisker plot of power usage per hour in the day.
1. Box and Whisker plot of power usage per hour in the day for weekdays only.
1. Box and Whisker plot of power usage per hour in the day for weekends only.

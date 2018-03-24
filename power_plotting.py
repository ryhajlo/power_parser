"""Class and methods for handling plotting of power data"""
import calendar
import matplotlib.pyplot as plt

class PowerPlotting(object):
    """Class for handling plotting of power data"""

    @staticmethod
    def get_data_to_plot(data):
        """Take a list of dictionaries with times and values,
        split data into two lists. Use this to plot data with matplotlib"""
        times = [d['time'] for d in data]
        values = [d['value'] for d in data]
        return times, values

    def plot_hourly_usage(self, usage_data=None, weekends=True, weekdays=True):
        """Plot power usage per hour of the day"""
        if usage_data:
            data_to_use = usage_data
        else:
            if self.usage_data:
                data_to_use = self.usage_data
            else:
                raise ValueError("No usage data provided")

        hours = [[] for _ in range(24)] #Initialize list by hours in a week
        for sample in data_to_use:
            #Count weekends if we are susposed to, and if it is a weekend
            if weekends and sample['time'].weekday() >= 5:
                hours[sample['time'].hour].append(sample['value'])
            elif weekdays and sample['time'].weekday() < 5:
                hours[sample['time'].hour].append(sample['value'])

        if weekends and weekdays:
            title = 'Power Usage Per Hour'
        elif weekends and not weekdays:
            title = 'Power Usage Per Hour for Weekends'
        elif not weekends and weekdays:
            title = 'Power Usage Per Hour for Weekdays'
        else:
            title = 'Power for neither weekdays or weekends?'

        labels = range(0, 24)
        PowerPlotting.__bot_plot(hours, labels, title=title)

    def plot_weekly_usage(self, usage_data=None):
        """Plot cummulative weekly usage data"""
        if usage_data:
            data_to_use = usage_data
        else:
            if self.usage_data:
                data_to_use = self.usage_data
            else:
                raise ValueError("No usage data provided")

        #Get the week number for the first sample.
        last_week = data_to_use[0]['time'].isocalendar()[1]
        #Initialize first week with time and empty usage
        weekly_data = [{'time': data_to_use[0]['time'], 'value': 0}]
        for sample in data_to_use:
            current_week = sample['time'].isocalendar()[1]
            if last_week != current_week:
                weekly_data.append({'time': sample['time'], 'value': sample['value']})
            else:
                #Within this week, add this sample's usage value
                weekly_data[-1]['value'] += sample['value']

            #Update current week index
            last_week = current_week
        times, values = PowerPlotting.get_data_to_plot(weekly_data)
        PowerPlotting.__scatter_plot(times, values, \
            title='Weekly Usage', x_label='Usage for week of')

    def plot_usage_per_week_day(self, usage_data=None):
        """Split data into usage per week day"""
        if usage_data:
            data_to_use = usage_data
        else:
            if self.usage_data:
                data_to_use = self.usage_data
            else:
                raise ValueError("No usage data provided")

        week_name_labels = list(calendar.day_name)
        days_per_week = len(week_name_labels) #helper variable
        week_days = [[] for _ in range(days_per_week)] #Initialize list by days in a week
        for sample in data_to_use:
            week_days[sample['time'].weekday()].append(sample['value'])

        PowerPlotting.__bot_plot(week_days, week_name_labels, title='Power Usage Day of Week')

    def plot_all_usage(self, usage_data=None):
        """Create a simple time series plot of all data"""
        if usage_data:
            data_to_use = usage_data
        else:
            if self.usage_data:
                data_to_use = self.usage_data
            else:
                raise ValueError("No usage data provided")

        times, values = PowerPlotting.get_data_to_plot(data_to_use)
        PowerPlotting.__scatter_plot(times, values)

    @staticmethod
    def __bot_plot(data, labels=None, title=None, y_label='Power Usage (kWh)', fliers=True):
        """Internal generation of box and whisker plot"""
        fig = plt.figure()
        axis = fig.add_subplot(111)
        axis.boxplot(data, showfliers=fliers)
        if title:
            axis.set_title(title)
        if labels:
            plt.xticks(range(1, len(labels)+1), labels)
        if y_label:
            plt.ylabel(y_label)

    @staticmethod
    def __scatter_plot(times, values, title='Power Usage', x_label=None):
        """Internal generation of scatter plot"""
        fig = plt.figure()
        axis = fig.add_subplot(111)
        plt.plot_date(times, values, '-o')
        plt.ylabel('Power Usage (kWh)')
        axis.set_title(title)
        if x_label:
            plt.xlabel(x_label)

    def show_plots(self):
        """Draw all plots"""
        plt.show()

    def __init__(self, usage_data=None):
        self.usage_data = usage_data

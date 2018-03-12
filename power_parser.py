#!/usr/bin/env python2
"""Take usage data .csv file from SCE, parse it, and analyze it"""
import sys
import os
import re
import datetime

def print_usage(error_string=""):
    """Print usage in the case of bad inputs"""
    script_name = os.path.basename(__file__)
    print "=========================="
    if error_string:
        print "Error: "
        print "\t " + error_string
    print "Usage: "
    print "\t" + script_name + " /path/to/usage.csv"
    print "=========================="
    raise ValueError("Incorrect Parameters")

def verify_inputs(args):
    """Verify the validity of the inputs.
       We need at least one argument, the csv file we are going to process."""
    if not args:
        print_usage(error_string="Not enough arguments")
        return False
    for csv_file_path in args:
        if not os.path.exists(csv_file_path):
            print_usage(error_string="Cannot locate file: " + str(csv_file_path))
            return False
    return True

def convert_date_dict_to_datetime(date_dict):
    """Take in a dictionary and return datetime"""
    return datetime.datetime(int(date_dict['year']), int(date_dict['month']), \
        int(date_dict['day']), int(date_dict['hour']), \
        int(date_dict['minute']), int(date_dict['second']))

def get_dates_from_line(csv_line):
    """Take in CSV line. If it is a line that contains two dates, extract and return them"""
    line_regex = re.compile(r'((?P<year>(?:19|20)\d\d)([- /.])' + \
        '(?P<month>0[1-9]|1[012])-(?P<day>0[1-9]|[12][0-9]|3[01])' + \
        '.(?P<hour>[0-1][0-9]|2[0-3]):(?P<minute>[0-5][0-9]):(?P<second>[0-5][0-9]))')
    dates = [m.groupdict() for m in line_regex.finditer(csv_line)]
    if len(dates) >= 2:
        #Make sure we get both a start and end time
        start_date = convert_date_dict_to_datetime(dates[0])
        end_date = convert_date_dict_to_datetime(dates[1])
        return [start_date, end_date]
    return None

def parse_csv_file(csv_path):
    """Read in a CSV file and return the data"""
    # This is only a CSV in that it's values are separted by commas.
    # There is a lot of non-tabular data in this file.
    consumption_data = []
    with open(csv_path) as csv_file_handle:
        for line in csv_file_handle:
            #Replace non-printable characters with a space
            line = re.sub(r'[^\x00-\x7F]+', ' ', line)
            times = get_dates_from_line(line)
            if times:
                split_line = line.split(",")
                #Second column contains usage data we are interested in
                consumption_value = float(split_line[1].replace('"', ''))
                #The end time is implied. Data is in one hour increments.
                consumption_data.append({'time': times[0], 'value': consumption_value})
    return consumption_data

def main(args):
    """Main function. Takes a list of csv filenames/paths"""
    verify_inputs(args)

    parsed_files = []
    for csv_file in args:
        parsed_files.append(parse_csv_file(csv_file))

    return True

if __name__ == "__main__":
    main(sys.argv[1:])

#!/usr/bin/env python2
"""Take usage data .csv file from SCE, parse it, and analyze it"""
import sys
import os

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

def main(args):
    """Main function. Takes a list of csv filenames/paths"""
    #We need at least one argument, the csv file we are going to process.
    if not args:
        print_usage(error_string="Not enough arguments")
    for csv_file_path in args:
        if not os.path.exists(csv_file_path):
            print_usage(error_string="Cannot locate file: " + str(csv_file_path))
        else:
            print csv_file_path + " exists"

    return True

if __name__ == "__main__":
    main(sys.argv[1:])

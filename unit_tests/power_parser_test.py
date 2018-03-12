"""Unit tests for power_parser"""
import datetime
import unittest
import power_parser

class TestPowerParserCSVParsing(unittest.TestCase):
    """Unit tests for parsing csv files"""
    def test_good_file_parsing(self):
        """Verify handling of not providing enough parameters"""
        usage_data = power_parser.parse_csv_file("unit_tests\\usage_data.csv")
        self.assertEqual(len(usage_data), 1311, "There are 1311 entries in the sample CSV file")
        #Check first entry
        self.assertEqual(usage_data[0]['value'], 0.79, \
            "Incorrect usage data for first entry. Expected 0.79 kWh, got " \
            + str(usage_data[0]['value']))
        self.assertEqual(usage_data[0]['time'], datetime.datetime(2018, 1, 1, 0, 0), \
            "Incorrect timestamp for first entry.")
        #Check last entry
        self.assertEqual(usage_data[-1]['value'], 0.24, \
            "Incorrect usage data for last entry. Expected 0.24 kWh, got " \
            + str(usage_data[-1]['value']))
        self.assertEqual(usage_data[-1]['time'], datetime.datetime(2018, 2, 24, 23, 0), \
            "Incorrect timestamp for last entry")

class TestPowerParserParameters(unittest.TestCase):
    """Unit tests for handling parameters from the command line"""
    def test_not_enough_parameters(self):
        """Verify handling of not providing enough parameters"""
        with self.assertRaises(ValueError):
            power_parser.verify_inputs([])

    def test_file_doesnt_exist(self):
        """Verify handling of providing a filename that doesn't exist"""
        with self.assertRaises(ValueError):
            power_parser.verify_inputs(["doesn_exist.csv"])

    def test_handle_good_file(self):
        """Verify handling of providing a filename that doesn't exist"""
        self.assertTrue(power_parser.verify_inputs(["unit_tests\\usage_data.csv"]))

    def test_handle_good_files(self):
        """Verify handling of providing a filename that doesn't exist"""
        self.assertTrue(power_parser.verify_inputs([\
            "unit_tests\\usage_data.csv", "unit_tests\\usage_data_old_apartment.csv"]))

if __name__ == '__main__':
    unittest.main()

"""Unit tests for power_parser"""
import unittest
import power_parser

class TestPowerParserParameters(unittest.TestCase):
    """Unit tests for handling parameters from the command line"""
    def test_not_enough_parameters(self):
        """Verify handling of not providing enough parameters"""
        with self.assertRaises(ValueError):
            power_parser.main([])

    def test_file_doesnt_exist(self):
        """Verify handling of providing a filename that doesn't exist"""
        with self.assertRaises(ValueError):
            power_parser.main(["doesn_exist.csv"])

    def test_handle_good_file(self):
        """Verify handling of providing a filename that doesn't exist"""
        self.assertTrue(power_parser.main(["unit_tests\\usage_data.csv"]))

    def test_handle_good_files(self):
        """Verify handling of providing a filename that doesn't exist"""
        self.assertTrue(power_parser.main([\
            "unit_tests\\usage_data.csv", "unit_tests\\usage_data_old_apartment.csv"]))

if __name__ == '__main__':
    unittest.main()

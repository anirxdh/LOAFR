import unittest
import pathlib
import sys
import datetime
directory = pathlib.Path(__file__)
sys.path.append(directory.parent.parent.parent.as_posix())
from src import hnl
#test cases for HNL

class TestHnl(unittest.TestCase):

    def setUp(self):
        self.hnl = hnl.Hnl()

    
    def test_apply_transform_normal_case(self):
        data = "04/01/2023 10:00:00, INFO, SENSOR, temperature, 15\n04/01/2023 10:05:00, INFO, SENSOR, temperature, 5\n04/01/2023 10:10:00, INFO, SENSOR, temperature, 25"
        event = "temperature"
        high = 20
        low = 10
        expected_output = "Duration: 0:05:00, Start: 2023-04-01 10:05:00, End: 2023-04-01 10:10:00\n"
        self.assertEqual(self.hnl.apply_transform(data, event, high, low), expected_output)


    def test_find_low_high_interval_no_intervals(self):
        data = "04/01/2023 10:00:00, INFO, SENSOR, temperature, 30"
        event = "temperature"
        high = 20
        low = 10
        self.assertEqual(list(self.hnl.find_low_high_interval(data, event, high, low)), [])

    def test_find_low_high_interval_multiple_intervals(self):
        data = "04/01/2023 10:00:00, INFO, SENSOR, temperature, 5\n04/01/2023 10:05:00, INFO, SENSOR, temperature, 25\n04/01/2023 10:10:00, INFO, SENSOR, temperature, 5\n04/01/2023 10:15:00, INFO, SENSOR, temperature, 25"
        event = "temperature"
        high = 20
        low = 10
        expected_intervals = [
            (datetime.datetime(2023, 4, 1, 10, 0, 0), datetime.datetime(2023, 4, 1, 10, 5, 0)),
            (datetime.datetime(2023, 4, 1, 10, 10, 0), datetime.datetime(2023, 4, 1, 10, 15, 0))
        ]
        self.assertEqual(list(self.hnl.find_low_high_interval(data, event, high, low)), expected_intervals)

    def test_apply_transform_invalid_data_format(self):
        data = "This is not a valid log format"
        event = "temperature"
        high = 20
        low = 10
        with self.assertRaises(ValueError):
            self.hnl.apply_transform(data, event, high, low)

    def test_apply_transform_edge_case_high_equals_low(self):
        data = "04/01/2023 10:00:00, INFO, SENSOR, temperature, 10"
        event = "temperature"
        high = 10
        low = 10
        expected_output = ""
        self.assertEqual(self.hnl.apply_transform(data, event, high, low), expected_output)

    # Additional test cases can be added as needed

if __name__ == "__main__":
    unittest.main()

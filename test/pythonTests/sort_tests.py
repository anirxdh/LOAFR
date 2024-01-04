import pathlib
import sys
import unittest
directory = pathlib.Path(__file__)
sys.path.append(directory.parent.parent.parent.as_posix())
from src import sort



class TestSearch(unittest.TestCase):
    
    def test_float_two_line_asc(self):
        data = "12/11/2023 08:50:01, INFO, insulin_pump, power on, 100.00\n12/22/2023 08:50:03, INFO, insulin_pump, read glucose, 75.95"
        column = 5
        direction = "asc"
        expected = "12/22/2023 08:50:03, INFO, insulin_pump, read glucose, 75.95\n12/11/2023 08:50:01, INFO, insulin_pump, power on, 100.00\n"
        result = sort.Sort().applyTransform(data, column, direction)
        self.assertEqual(result, expected)

    def test_float_two_line_desc(self):
        data = "12/11/2023 08:50:01, INFO, insulin_pump, power on, 100.00\n12/22/2023 08:50:03, INFO, insulin_pump, read glucose, 75.95"
        column = 5
        direction = "desc"
        expected = "12/11/2023 08:50:01, INFO, insulin_pump, power on, 100.00\n12/22/2023 08:50:03, INFO, insulin_pump, read glucose, 75.95\n"
        result = sort.Sort().applyTransform(data, column, direction)
        self.assertEqual(result, expected)

    def test_datetime_multi_line(self):
        data = "12/22/2023 08:50:03, INFO, insulin_pump, read glucose, 75.95\n12/11/2023 08:50:01, INFO, insulin_pump, power on, 100.00\n12/22/2023 09:00:03, INFO, insulin_pump, read glucose, 77.95\n12/22/2023 08:55:05, INFO, insulin_pump, read glucose, 80.95"
        column = 1
        direction = "asc"
        expected = "12/11/2023 08:50:01, INFO, insulin_pump, power on, 100.00\n12/22/2023 08:50:03, INFO, insulin_pump, read glucose, 75.95\n12/22/2023 08:55:05, INFO, insulin_pump, read glucose, 80.95\n12/22/2023 09:00:03, INFO, insulin_pump, read glucose, 77.95\n"
        result = sort.Sort().applyTransform(data, column, direction)
        self.assertEqual(result, expected)

    def test_text_multi_line(self):
        data = "12/11/2023 08:50:01, INFO, insulin_pump, power on, 100.00\n12/22/2023 09:25:00, WARN, insulin_pump, failed to read glucose\n12/22/2023 09:30:20, INFO, insulin_pump, check resevoirs, 80.60, 99.98\n12/22/2023 16:01:02, WARN, insulin_pump, low resevoir"
        column = 4
        direction = "asc"
        expected = "12/22/2023 09:30:20, INFO, insulin_pump, check resevoirs, 80.60, 99.98\n12/22/2023 09:25:00, WARN, insulin_pump, failed to read glucose\n12/22/2023 16:01:02, WARN, insulin_pump, low resevoir\n12/11/2023 08:50:01, INFO, insulin_pump, power on, 100.00\n"
        result = sort.Sort().applyTransform(data, column, direction)
        self.assertEqual(result, expected)
    

if __name__ =="__main__":
    unittest.main()
    
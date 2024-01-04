import pathlib
import sys
import unittest
directory = pathlib.Path(__file__)
sys.path.append(directory.parent.parent.parent.as_posix())
from src import condition
from src import after

class TestAfter(unittest.TestCase):
    def test_noneBeforeNoneAfter(self):
        data = ""

        cond = condition.Condition("< .6")

        transform = after.After()

        output = transform.apply_transform(data, cond)

        expected = ""
        self.assertEqual(output, expected)

    def test_noneBeforeSomeAfter(self): 
        data = """12/22/2023 09:25:03, INFO, insulin_pump, read glucose, 105.28
12/22/2023 09:25:01, INFO, insulin_pump, pump insulin, 1.00
12/22/2023 09:30:03, INFO, insulin_pump, read glucose, 96.66
12/22/2023 09:30:20, INFO, insulin_pump, check resevoirs, 80.60, 99.98
12/22/2023 09:35:03, INFO, insulin_pump, read glucose, 73.43
12/22/2023 16:01:00, INFO, insulin_pump, low resevoir
12/22/2023 16:01:02, WARN, insulin_pump, low resevoir
"""

        cond = condition.Condition("> 102.2")

        transform = after.After()

        output = transform.apply_transform(data, cond)

        expected = """12/22/2023 09:25:03, INFO, insulin_pump, read glucose, 105.28
12/22/2023 09:25:01, INFO, insulin_pump, pump insulin, 1.00
12/22/2023 09:30:03, INFO, insulin_pump, read glucose, 96.66
12/22/2023 09:30:20, INFO, insulin_pump, check resevoirs, 80.60, 99.98
12/22/2023 09:35:03, INFO, insulin_pump, read glucose, 73.43
12/22/2023 16:01:00, INFO, insulin_pump, low resevoir
12/22/2023 16:01:02, WARN, insulin_pump, low resevoir

"""
        self.assertCountEqual(output, expected)
        # self.assertAlmostEqual(output, expected)

    def test_someBeforeNoneAfter(self): 
        data = """12/11/2023 08:50:01, INFO, insulin_pump, power on, 100.00
12/22/2023 08:50:03, INFO, insulin_pump, read glucose, 75.95
12/22/2023 08:55:05, INFO, insulin_pump, read glucose, 80.95
12/22/2023 09:00:03, INFO, insulin_pump, read glucose, 77.95
12/22/2023 09:05:01, INFO, insulin_pump, check power, 98.98
12/22/2023 09:05:03, INFO, insulin_pump, read glucose, 75.60
12/22/2023 09:10:03, INFO, insulin_pump, read glucose, 73.00
12/22/2023 09:15:03, INFO, insulin_pump, read glucose, 85.95
12/22/2023 09:20:04, INFO, insulin_pump, read glucose, 99.10
12/22/2023 09:25:00, WARN, insulin_pump, failed to read glucose
"""

        cond = condition.Condition("> 102.2")

        transform = after.After()

        output = transform.apply_transform(data, cond)

        expected = """"""
        self.assertCountEqual(output, expected)

    def test_someBeforeSomeAfter(self): 
        data = """12/11/2023 08:50:01, INFO, insulin_pump, power on, 100.00
12/22/2023 08:50:03, INFO, insulin_pump, read glucose, 75.95
12/22/2023 08:55:05, INFO, insulin_pump, read glucose, 80.95
12/22/2023 09:00:03, INFO, insulin_pump, read glucose, 77.95
12/22/2023 09:05:01, INFO, insulin_pump, check power, 98.98
12/22/2023 09:05:03, INFO, insulin_pump, read glucose, 75.60
12/22/2023 09:10:03, INFO, insulin_pump, read glucose, 73.00
12/22/2023 09:15:03, INFO, insulin_pump, read glucose, 85.95
12/22/2023 09:20:04, INFO, insulin_pump, read glucose, 99.10
12/22/2023 09:25:00, WARN, insulin_pump, failed to read glucose
12/22/2023 09:25:03, INFO, insulin_pump, read glucose, 105.28
12/22/2023 09:25:01, INFO, insulin_pump, pump insulin, 1.00
12/22/2023 09:30:03, INFO, insulin_pump, read glucose, 96.66
12/22/2023 09:30:20, INFO, insulin_pump, check resevoirs, 80.60, 99.98
12/22/2023 09:35:03, INFO, insulin_pump, read glucose, 73.43
12/22/2023 16:01:00, INFO, insulin_pump, low resevoir
12/22/2023 16:01:02, WARN, insulin_pump, low resevoir
"""

        cond = condition.Condition("> 102.2")

        transform = after.After()

        output = transform.apply_transform(data, cond)

        expected = """12/22/2023 09:25:03, INFO, insulin_pump, read glucose, 105.28
12/22/2023 09:25:01, INFO, insulin_pump, pump insulin, 1.00
12/22/2023 09:30:03, INFO, insulin_pump, read glucose, 96.66
12/22/2023 09:30:20, INFO, insulin_pump, check resevoirs, 80.60, 99.98
12/22/2023 09:35:03, INFO, insulin_pump, read glucose, 73.43
12/22/2023 16:01:00, INFO, insulin_pump, low resevoir
12/22/2023 16:01:02, WARN, insulin_pump, low resevoir

"""
        self.assertCountEqual(output, expected)

if __name__ =="__main__":
    unittest.main()
    
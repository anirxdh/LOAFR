import pathlib
import sys
import unittest
directory = pathlib.Path(__file__)
sys.path.append(directory.parent.parent.parent.as_posix())

from src import logfile

class TestLogfile(unittest.TestCase):
    
    # Method: Read()
    def test_read_single_word(self):
        l = logfile.Logfile('test/expected/single_word.log')
        self.assertEqual(l.Read(), 'loafr')
        
    def test_read_multiple_lines(self):
        l = logfile.Logfile('test/expected/all_lines.log')
        with open('test/expected/all_lines.log') as f:
            expected = f.read()
        self.assertEqual(l.Read(), expected)

if __name__ == "__main__":
    unittest.main()
import pathlib
import sys
import unittest
directory = pathlib.Path(__file__)
sys.path.append(directory.parent.parent.parent.as_posix())
from src import search



class TestSearch(unittest.TestCase):
    
    def test_search_found_oneLine_oneKeyword(self):
        data = "loafr test"
        keywords = ["loafr"]
        expected = "loafr test\n"
        result = search.Search().applyTransform(data, keywords)
        self.assertEqual(result, expected)
        
    def test_search_found_twoLines_oneKeyword(self):
        data = "loafr test\nsecond test line"
        keywords = ["loafr"]
        expected = "loafr test\n"
        result = search.Search().applyTransform(data, keywords)
        self.assertEqual(result, expected)
        
    def test_search_found_twoLines_twoKeywords(self):
        data = "loafr test\nsecond test line"
        keywords = ["loafr", "second"]
        expected = "loafr test\nsecond test line\n"
        result = search.Search().applyTransform(data, keywords)
        self.assertEqual(result, expected)
    def test_search_emptyLogAndKeywords(self):
        # Test case for empty log data and empty keywords
        data = ""
        keywords = []
        expected = ""
        result = search.Search().applyTransform(data, keywords)
        self.assertEqual(result, expected)
        
    def test_search_logDataNoKeywords(self):
        # Test case for log data with no provided keywords
        data = "loafr test\nsecond test line"
        keywords = [""]
        expected = "loafr test\nsecond test line\n"
        result = search.Search().applyTransform(data, keywords)
        self.assertEqual(result, expected)
        
    def test_search_noMatchesForKeywords(self):
        # Test case for no matches found for given keywords
        data = "loafr test\nsecond test line"
        keywords = ["random", "keyword"]
        expected = ""
        result = search.Search().applyTransform(data, keywords)
        self.assertEqual(result, expected)

if __name__ =="__main__":
    unittest.main()
    
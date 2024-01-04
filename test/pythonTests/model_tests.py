import pathlib
import sys
import unittest
directory = pathlib.Path(__file__)
sys.path.append(directory.parent.parent.parent.as_posix())
from src import model
from src import options


class TestModel(unittest.TestCase):
    
    # Method: AddLogfile(path) -> bool
    def test_addlogfile_file_exists_added(self):
        m = model.Model()
        path = 'test/test.log'
        m.AddLogfile(path)
        added = False
        for log in m.inputLogfiles:
            if log.path == path:
                added = True
        self.assertTrue(added)
    
    def test_addlogfile_file_exists_return_value(self):
        m = model.Model()
        path = 'test/test.log'
        self.assertTrue(m.AddLogfile(path))

    def test_addlogfile_file_does_not_exist(self):
        m = model.Model()
        path = 'test/test.xyz'
        self.assertFalse(m.AddLogfile(path))
        
    def test_addlogfile_empty_path(self):
        m = model.Model()
        path = ''
        self.assertFalse(m.AddLogfile(path))
        
    # Method: RemoveLogfile(filename) -> bool
    def test_removelogfile_file_exists_removed(self):
        m = model.Model()
        path = 'test/test.log'
        m.AddLogfile(path)
        m.RemoveLogfile(path)
        for log in m.inputLogfiles:
            self.assertNotEqual(log.filename, path)
        
    def test_removelogfile_file_exists_return_value(self):
        m = model.Model()
        path = 'test/test.log'
        m.AddLogfile(path)
        self.assertTrue(m.RemoveLogfile(path))
        
    def test_removelogfile_file_does_not_exist(self):
        m = model.Model()
        path = 'test/test.log'
        m.AddLogfile(path)
        self.assertFalse(m.RemoveLogfile('test/test.xyz'))
        
    def test_removelogfile_file_empty_path(self):
        m = model.Model()
        path = 'test/test.log'
        m.AddLogfile(path)
        self.assertFalse(m.RemoveLogfile(''))
        
    # Method: GetOptions() -> Options
    def test_getoptions(self):
        m = model.Model()
        o = options.Options()
        m.SetOptions(o)
        self.assertIsInstance(m.GetOptions(), options.Options)
        
    def test_getoptions_null(self):
        m = model.Model()
        self.assertEqual(None, m.GetOptions())
        
    # Method: SetOptions(options)
    def test_setoptions(self):
        m = model.Model()
        o = options.Options()
        m.SetOptions(o)
        self.assertEqual(m.GetOptions(), o)
        
    def test_setoptions_type_error(self):
        m = model.Model()
        x = model.Model()
        self.assertRaises(TypeError, m.SetOptions(x))

if __name__ == "__main__":
    unittest.main()
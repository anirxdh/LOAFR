import pathlib
import sys
import unittest
directory = pathlib.Path(__file__)
sys.path.append(directory.parent.parent.parent.as_posix())
from src import model
from src import viewcli

class TestViewCLI(unittest.TestCase):
    
    # Method: RegisterModel
    def test_register_model(self):
        m = model.Model()
        v = viewcli.ViewCLI()
        v.register_model(m)
        self.assertIsInstance(v.instance_model, model.Model)
        
    def test_register_model_return_value(self):
        m = model.Model()
        v = viewcli.ViewCLI()
        self.assertEqual(v.register_model(m), m)
        
    def test_register_model_bad_model(self):
        x = viewcli.ViewCLI()
        v = viewcli.ViewCLI()
        self.assertRaises(TypeError, v.register_model(x))
        
    def test_register_model_none(self):
        x = None
        v = viewcli.ViewCLI()
        self.assertRaises(TypeError, v.register_model(x))
    
    # Method: GetModel
    def test_get_model(self):
        m = model.Model()
        v = viewcli.ViewCLI()
        v.register_model(m)
        self.assertEqual(m, v.get_model())
    
    def test_get_model_none(self):
        v = viewcli.ViewCLI()
        v.register_model(None)
        self.assertEqual(None, v.get_model())

if __name__ == "__main__":
    unittest.main()
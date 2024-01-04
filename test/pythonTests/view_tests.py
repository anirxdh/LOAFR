import pathlib
import sys
import unittest
directory = pathlib.Path(__file__)
sys.path.append(directory.parent.parent.parent.as_posix())
from src import view
from src import model

class TestView(unittest.TestCase):
    
    # Method: RegisterModel
    def test_register_model_instance(self):
        m = model.Model()
        v = view.View()
        v.register_model(m)
        self.assertIsInstance(v.instance_model, model.Model)
        
    def test_register_model_return_value(self):
        m = model.Model()
        v = view.View()
        self.assertEqual(v.register_model(m), m)
        
    def test_register_model_bad_model(self):
        x = view.View()
        v = view.View()
        self.assertRaises(TypeError, v.register_model(x))
        
    def test_register_model_none(self):
        x = None
        v = view.View()
        self.assertRaises(TypeError, v.register_model(x))
    
    # Method: GetModel
    def test_get_model(self):
        m = model.Model()
        v = view.View()
        v.register_model(m)
        self.assertEqual(m, v.get_model())
    
    def test_get_model_none(self):
        v = view.View()
        v.register_model(None)
        self.assertEqual(None, v.get_model())

if __name__ == "__main__":
    unittest.main()
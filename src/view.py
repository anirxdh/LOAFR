'''MVC View 

Provides a view component to display information about the state of the LOAFR
system to the user. Only a command line view is available as of the current
version (see: viewcli.py).
'''
from src import model

class View:
    
    instance_model : model.Model
    
    def __init__(self):
        return
    
    def register_model(self, model : model.Model) -> model.Model:
        '''Registers a model for this view to send updates to.
        
        Args:
            model: The model to register to this view.
            
        Returns:
            The model that has been registered to the view.
        '''
        self.instance_model = model
        return self.instance_model
    
    def get_model(self) -> model.Model:
        '''Gets the model registered to this view.
        
        Returns:
            The model object registered to this view.
        '''
        return self.instance_model

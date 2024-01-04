import os
from src.logfile import Logfile
from src.options import Options

class Model:
    
    inputLogfiles : list[Logfile] = []
    outputLogfile : None | Logfile = None
    instance_options : Options = None
    
    def __init__(self):
        return
    
    def AddLogfile(self, path : str) -> bool:
        '''Add a logfile to the LOAFR model.
        
        Args:
            path: The full path to the log file that should be added.
            
        Returns:
            True if the log file was successfully added.
            False if the log file could not be added.
        '''
        if (os.path.isfile(path)):
            self.inputLogfiles.append(Logfile(path))
            return True
        return False
    
    def RemoveLogfile(self, path : str) -> bool:
        '''Remove a logfile from the LOAFR model.
        
        Args:
            path: The path of the log file to remove.
        
        Returns:
            True if a log file was removed.
            False if no log file was removed.
        '''
        retVal = False
        
        for log in self.inputLogfiles:
            if (log.path == path):
                self.inputLogfiles.remove(log)
                retVal = True
                
        return retVal
    
    def GetOptions(self):
        return self.instance_options
    
    def SetOptions(self, options):
        self.instance_options = options
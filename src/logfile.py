from src.logfileconfig import LogfileConfig
from datetime import datetime

class Logfile:
    
    path : None | str = None
    filename : None | str = None
    config : None | LogfileConfig
    
    def __init__(self, path):
        self.path = path

    def read(self) -> str:
        '''Read data from a log file into a string.
        
        Returns:
            A string containing the entirety of a log file's contents.
            
        Todo:
            Move the reading the log file into the analysis functions, so log
            files are parsed line by line and we can support large log files.
        '''
        f = open(self.path, "r")
        data = f.read()
        f.close()
        return data
    
    def append(self, data):
        '''Writes data to the end of a log file.
        
        Returns:
            This Logfile object.
        '''
        f = open(self.path, "a")
        f.write(data)
        f.close()
        return self
    
    @classmethod
    def parse_line(self, line : str):
        '''Parse a log file line into its component parts.
        
        Args:
            line: The line within a log file to parse.
            
        Returns:
            An n-tuple containing the component parts of the log entry.
            
        TODO: Do this dynamically using log file configurations.
        '''
        if line == "":
            return "", "", "", "", ""
        
        parts = line.strip().split(",")
        if (len(parts) > 0):
            timestamp = datetime.strptime(parts[0], "%m/%d/%Y %H:%M:%S")
            log_level = parts[1]
            log_source = parts[2]
            event_type = parts[3]
            value = parts[4:]
            return timestamp, log_level, log_source, event_type, value
        return "", "", "", "", ""
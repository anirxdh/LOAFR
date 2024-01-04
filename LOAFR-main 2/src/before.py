from src.logfile import Logfile
from src.condition import Condition

class Before:
    
    def __init__(self):
        self.output = ""
        return

    def apply_transform(self, data, condition : Condition) -> str:
        '''Writes only log file entries occuring before a condition has been met
            to the output file.
            
        Args:
            data: The log file data. TODO: Pass in Logfile object instead.
            condition: A condition which must be met to begin writing output.
            
        Returns:
            A log file string containing the contents of the input log file, 
            with lines occuring after the condition omitted.
        '''
        if data.strip() == "":
            return ""
        
        for line in data.split('\n'):
            
            # Grab the value from this liine
            _, _, _, _, value = Logfile.parse_line(line)
            
            if not value or value == "":
                self.output += line + '\n'
                continue
            
            # Check if the start condition has been met
            # For now, assume all values can be cast as floats
            if (condition.check(float(value[0]))):
                break
    
            self.output += line + '\n'
                
        return self.output
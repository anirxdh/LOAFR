from src.logfile import Logfile
from src.condition import Condition

class After:
    
    def __init__(self):
        self.output = ""
        return

    def apply_transform(self, data, condition : Condition) -> str:
        '''Writes only log file entries occuring after a condition has been met
            to the output file.
            
        Args:
            data: The log file data. TODO: Pass in Logfile object instead.
            condition: A condition which must be met to begin writing output.
            
        Returns:
            A log file string containing the contents of the input log file, 
            with lines occuring before the condition omitted.
        '''
        if data.strip() == "":
            return ""
        
        in_context = False
        for line in data.split('\n'):
            
            # Grab the value from this liine
            _, _, _, _, value = Logfile.parse_line(line)
            
            if not value or value == "":
                if in_context:
                    self.output += line + '\n'
                continue
            
            # Check if the start condition has been met
            # For now, assume all values can be cast as floats
            if (condition.check(float(value[0]))):
                in_context = True
    
            # If we're after the point the condition has been met, start logging
            # to the output file
            if in_context:
                self.output += line + '\n'
                
        return self.output
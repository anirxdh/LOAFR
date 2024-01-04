from datetime import datetime

class Sort:
    def __init__(self):
        self.output = ""
        
    def applyTransform(self, data : str, column : int, direction : str) -> str:
        '''Search log entries for keywords.
        
        Args:
            data: Log file in string format. 
        
            column: The column being sorted

            direction: The direction the specified column will be sorted in
            
        Returns:
            A string version of the log file with the only the sorted content
        '''
        #Strip to array of array of words in row
        rows = [line.strip().split(', ') for line in data.strip().split('\n')]

        #Remove rows that don't have specified column
        filtered_rows = [row for row in rows if len(row) > column-1]

        #Get direction
        if direction == "desc":
            reversed = True
        else:
            reversed = False

        #Sort according to content
        sorted_rows = sorted(filtered_rows, key=lambda x: convert_to_float(x[column-1]), reverse=reversed)
        
        #Build/Format output
        self.output = '\n'.join([', '.join(row) for row in sorted_rows])
        self.output += '\n'
        
        return self.output
    
def convert_to_float(value):
    try:
        return float(value)
    except:
        return value
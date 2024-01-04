class Count:
    def __init__(self):
        self.outputCount = 0
        self.outputRows = ""
        
    def applyTransform(self, data : str, keyword : str) -> str:
        '''Search log entries for keywords and count the amount of occurences.
        
        Args:
            data: Log file in string format. TODO: Passing a string in might not
                    be efficient. Pass in log path and read the file here.
        
            keyword: The keyword to search for.
            
        Returns:
            A string version of the log file with only rows containing the key
            words, prefixed by "COUNT of {keyword}"
        '''
        
        data = data.split("\n")
        for row in data:
            if keyword in row:
                self.outputCount += 1
                self.outputRows += row + "\n"
        
        return f"COUNT of {keyword}, {self.outputCount}\n{self.outputRows}"
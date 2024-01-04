class Search:
    def __init__(self):
        self.output = ""
        
    def applyTransform(self, data : str, keywords : list) -> str:
        '''Search log entries for keywords.
        
        Args:
            data: Log file in string format. TODO: Passing a string in might not
                    be efficient. Pass in log path and read the file here.
        
            keywords: A list of keywords to search for.
            
        Returns:
            A string version of the log file with only rows containing the key
            words.
        '''
        
        data = data.split("\n")
        for row in data:
            if any(keyword in row for keyword in keywords):
                self.output += row + "\n"
        
        return self.output
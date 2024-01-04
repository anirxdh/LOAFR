'''Command line interface view

Provides a view component to display information about the state of the LOAFR
system to the user. Only a command line view is available as of the current
version. Extends View (see: view.py).
'''
from src import view
from src import options

class ViewCLI(view.View):
    
    def __init__(self):
        super().__init__()
        return
    
    def PromptInputLogfiles(self):
        '''Gets a list of log file paths to send to the model via the controller.
        
        Returns:
            A list of paths to log files that should be added to the LOAFR model.
        '''
        logfiles : list(str) = []
        print("Please enter the full path to a log file to add to LOAFR.")
        print("To finish, press ENTER.")
        path = "x"
        while (path):
            path = input("Logfile path: ")
            super().get_model().AddLogfile(path)
        return logfiles

    def PromptOptions(self) -> options.Options:
        '''Gets some options for running analysis on log files.
        
        Returns:
            A dictionary mapping analysis methods and their options.
        '''
        opts = options.Options()
        validTransforms = {
            "search": "Enter the keyword(s) to be searched for, separated by commas (<keyword_1>, <keyword_2>, ... <keyword_n>): ",
            "filter": "Enter the columns to be filtered out, separated by commas (col_1, col_2, ... col_n): ",
            "count": "Enter the keyword that you would like to be counted: ",
            "hnl": "Enter the event you would like to find a high-low range for, followed by the high and low values (<event_type>, <high>, <low>): ",
            "after": "Enter the conditional statement the value must meet to begin context for output ([<|<=|==|>=|>|!=] [VALUE]): ",
            "before": "Enter the conditional statement the value must meet to end context for output ([<|<=|==|>=|>|!=] [VALUE]): ",
            "sort": "\nEnter the column number to be sorted, a comma, and the direction ([1|2|3|...]), [asc|desc].\nOnly rows containing the specified column will be sorted, and all datatypes MUST be the same: "
        }
        
        # Get the functions to apply to the log files
        while True:
            transform = input("Please enter the function you would like to apply (SEARCH, COUNT, HNL, AFTER, BEFORE, SORT), or press ENTER to continue: ").lower()
            if transform in validTransforms.keys():
                param = input(validTransforms[transform])
                opts.setOption(transform, param)
            elif transform == "":
                break
            else:
                print("Invalid transform provided. Would you like to continue entering transforms? (y/n): ")
                if "n" == input().lower():
                    break
                
        path = input("Enter an output path for the analysis file: ")
        opts.setOutputPath(path)
        
        super().get_model().SetOptions(opts)
        return opts
import sys
from . import model
from . import view
from . import viewcli
from . import analyzer

class Controller:
    
    instance_model : model.Model | None
    instance_view : viewcli.ViewCLI | view.View | None
    
    def __init__(self, m : model.Model, v : viewcli.ViewCLI):
        
        self.instance_model = m
        self.instance_view = v
                
        if (len(sys.argv) > 2):
            # Batch process log files - not implemented
            print("Batch processing detected - not implemented")
            return
        
        if (type(self.instance_view) == viewcli.ViewCLI):
            self.RunCLI()
        
        return
    
    def RunCLI(self) -> None:
        '''Runs the command line interface mode of LOAFR.
        
        Links the view with LOAFR's model for sharing data on updates. Then gets
        data by prompting the user through the command line interface for:
            - A list of log files to include in the analysis.
            - A selection of which analyses should be run on the log files.
            - A destination to write the output analysis log file to.
        Then, runs analysis on the log files using the user's input, and writes
        the resulting output log file.
        
        Returns:
            None
        '''
        self.instance_view.register_model(self.instance_model) # Link view->model
        self.instance_view.PromptInputLogfiles() # Get log files for analysis
        self.instance_view.PromptOptions() # Get analysis options
        log_analyzer = analyzer.Analyzer(self.instance_model) # Instantiate analyzer
        log_analyzer.Analyze() # Run analysis
        return

#     def sort_log(logfile, column_index):
#     # Read the log file and store its lines
#         with open(logfile, 'r') as file:
#             lines = file.readlines()

#     # Sort the lines based on the user-provided column index
#         sorted_lines = sorted(lines, key=lambda x: x.split(',')[column_index].strip())

#     # Write the sorted lines to a new log file
#         with open("sorted_logfile.log", 'w') as sorted_file:
#             sorted_file.writelines(sorted_lines)


#     def filter_log(logfile, condition):
#     # Read the log file and store its lines
#         with open(logfile, 'r') as file:
#             lines = file.readlines()

#     # Apply filter condition and get filtered lines
#         filtered_lines = []
#         for line in lines:
#             if condition in line:
#                 filtered_lines.append(line)

#         return filtered_lines
from src import model
from src import search
from src import logfile
from src import count
from src import hnl
from src import after
from src import before
from src import condition
from src import sort

class Analyzer:
    
    instance_model : model.Model
    
    def __init__(self, m):
        self.instance_model = m
        
    def Analyze(self):
        '''Perform the user's requested analyses on the log files.
        '''
        opts = self.instance_model.GetOptions()
        output = logfile.Logfile(opts.outputPath)
        data = ""
        for log in self.instance_model.inputLogfiles:
            data += log.read()
        
        # TODO: This should create a transform object for each transformation
        #       the user set in the options, then use that transform object's
        #       applyTransform method
        for transform in opts.transforms:
            if (transform == "search"):
                transformation = search.Search()
                keywords = opts.searchValues
                data = transformation.applyTransform(data, keywords)
            elif (transform == "count"):
                transformation = count.Count()
                keyword = opts.countKeyword
                data = transformation.applyTransform(data, keyword)
            elif (transform == "hnl"):
                transformation = hnl.Hnl()
                data = transformation.apply_transform(data, opts.hnlEvent, opts.hnlHigh, opts.hnlLow)
            elif (transform == "after"):
                transformation = after.After()
                cond = condition.Condition(opts.afterCondition)
                data = transformation.apply_transform(data, cond)
            elif (transform == "before"):
                transformation = before.Before()
                cond = condition.Condition(opts.beforeCondition)
                data = transformation.apply_transform(data, cond)
            elif (transform == "sort"):
                transformation = sort.Sort()
                column = int(opts.sortColumn)
                direction = opts.sortDirection
                data = transformation.applyTransform(data, column, direction)

                    
        output.append(data)
        return
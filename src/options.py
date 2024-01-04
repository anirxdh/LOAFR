class Options:
    
    searchValues : list
    sortColumns : list
    sortDirections : list
    filterColumns : list
    filterValues : list
    outputPath : str
    hnlEvent : str
    hnlHigh : float
    hnlLow : float
    afterCondition : str
    transforms : list
    
    def __init__(self):
        self.searchValues = []
        self.countKeyword = ""
        self.sortColumn = -1
        self.sortDirection = ""
        self.filterColumns = []
        self.filterValues = []
        self.hnlEvent = ""
        self.hnlHigh = -1.0
        self.hnlLow = 99999.999
        self.afterCondition = ""
        self.beforeCondition = ""
        self.transforms = []

    def setOption(self, transform : str, parameter):
        if "search" == transform.lower():
            self.transforms.append("search")
            tempParams = parameter.split(",")
            for parameter in tempParams:
                self.searchValues.append(parameter)
        elif "count" == transform.lower():
            if parameter == "":
                print("Please enter a valid term(s)")
            else: 
                self.transforms.append("count")
                self.countKeyword = parameter
        elif "hnl" == transform.lower():
            self.transforms.append("hnl")
            tempParams = parameter.split(",")
            self.hnlEvent = tempParams[0].strip()
            self.hnlHigh = float(tempParams[1].strip())
            self.hnlLow = float(tempParams[2].strip())
        elif "after" == transform.lower():
            self.transforms.append("after")
            self.afterCondition = parameter
        elif "before" == transform.lower():
            self.transforms.append("before")
            self.beforeCondition = parameter
        elif "sort" == transform.lower():
            self.transforms.append("sort")
            tempParams = parameter.split(", ")
            self.sortColumn = tempParams[0].strip()
            self.sortDirection = tempParams[1].strip()
                
    def setOutputPath(self, path):
        self.outputPath = path
        return
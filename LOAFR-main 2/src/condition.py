class Condition:
    
    operator : str
    value : str
    
    def __init__(self, condition : str):
        operator, value = condition.strip().split(' ')
        self.operator = operator
        self.value = value
        return
    
    def check(self, arg : float):
        if self.operator == "<":
            return arg < float(self.value)
        elif self.operator == "<=":
            return arg <= float(self.value)
        elif self.operator == "==":
            return arg == float(self.value)
        elif self.operator == ">=":
            return arg >= float(self.value)
        elif self.operator == ">":
            return arg > float(self.value)
        elif self.operator == "!=":
            return arg != float(self.value)
        else:
            return False
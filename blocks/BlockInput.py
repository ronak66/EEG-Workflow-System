class BlockInput:

    def __init__(self,name:str, min_cardinality:int, max_cardinality:int, parameter_type:str):
        if not (isinstance(name,str) and isinstance(min_cardinality,int) and isinstance(max_cardinality,int) \
            and isinstance(parameter_type,str)):
            raise TypeError("Incorrect parameter type")
        self.name = name
        self.value = None
        self.min_cardinality = min_cardinality
        self.max_cardinality = max_cardinality
        self.parameter_type = parameter_type

    def set_value(self,value):
        self.value = value
class BlockParameter:

    def __init__(self, name:str, parameter_type:str):
        if not (isinstance(name,str) and isinstance(parameter_type,str)):
            raise TypeError("Incorrect parameter type")
        self.name = name
        self.value = None
        self.parameter_type = parameter_type

    def set_value(self,value):
        self.value = value
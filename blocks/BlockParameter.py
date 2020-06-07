class BlockParameter:

    def __init__(self, name:str, value, parameter_type:str):
        if not (isinstance(name,str) and isinstance(parameter_type,str)):
            raise TypeError("Incorrect parameter type")
        self.name = name
        self.value = value
        self.parameter_type = parameter_type
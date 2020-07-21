class BlockParameter:

    def __init__(self, name:str, attribute_type:str, defaultvalue=None, description=''):
        if not (isinstance(name,str) and isinstance(attribute_type,str)):
            raise TypeError("Incorrect parameter type")
        self.name = name
        self.value = defaultvalue
        self.attribute_type = attribute_type
        self.description = str(description)

    def set_value(self,value):
        self.value = value
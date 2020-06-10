class BlockOutput:

    def __init__(self, name:str, attribute_type:str, min_cardinality:int, max_cardinality:int):
        if not (isinstance(name,str) and isinstance(min_cardinality,int) and isinstance(max_cardinality,int) \
            and isinstance(attribute_type,str)):
            raise TypeError("Incorrect parameter type")
        self.name = name
        self.value = None
        self.max_cardinality = max_cardinality
        self.min_cardinality = min_cardinality
        self.attribute_type = attribute_type

    def set_value(self,value):
        self.value = value
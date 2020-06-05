class BlockInput:

    def __init__(self,name:str, value, min_cardinality:int, max_cardinality:int, input_type:str):
        self.name = name
        self.value = value
        self.min_cardinality = min_cardinality
        self.max_cardinality = max_cardinality
        self.input_type = input_type
class BlockOutput:

    def __init__(self, name:str, value, output_type:str, min_cardinality:int, max_cardinality:int):
        self.name = name
        self.value = value
        self.max_cardinality = max_cardinality
        self.min_cardinality = min_cardinality
        self.output_type = output_type
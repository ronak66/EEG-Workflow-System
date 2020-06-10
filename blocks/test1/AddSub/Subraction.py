from blocks.Block import Block 
from blocks.BlockInput import BlockInput
from blocks.BlockParameter import BlockParameter
from blocks.BlockOutput import BlockOutput

class Subraction(Block):

    family = 'AddSub'
    name = 'Subraction'

    def __init__(self):
        self.num1 = BlockInput(
            name='num1',
            min_cardinality=1,
            max_cardinality=1,
            parameter_type='int'
        )
        self.num2 = BlockInput(
            name='num2',
            min_cardinality=1,
            max_cardinality=1,
            parameter_type='int'
        )
        self.output = BlockOutput(
            name='output',
            min_cardinality=1,
            max_cardinality=1,
            parameter_type='int'
        )
        

    def input_params(self,num1,num2):
        self.num1.set_value(num1)
        self.num2.set_value(num2)

    def execute(self):
        value = self.num1.value - self.num2.value
        self.output.set_value(value)
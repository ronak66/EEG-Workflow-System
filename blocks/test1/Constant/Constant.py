from blocks.Block import Block 
from blocks.BlockInput import BlockInput
from blocks.BlockParameter import BlockParameter
from blocks.BlockOutput import BlockOutput

class Constant(Block):

    family = 'Constant'
    name = 'Constant'

    def __init__(self):
        self.num = BlockParameter(
            name='constant value',
            parameter_type='int',
            defaultvalue=10
        )
        self.output = BlockOutput(
            name='output',
            min_cardinality=1,
            max_cardinality=1,
            parameter_type='int'
        )

    def input_params(self,const_value):
        self.num.set_value(const_value)

    def execute(self):
        value = self.num.value
        self.output.set_value(value)
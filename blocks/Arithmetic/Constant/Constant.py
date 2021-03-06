from blocks.Block import Block 
from blocks.BlockInput import BlockInput
from blocks.BlockParameter import BlockParameter
from blocks.BlockOutput import BlockOutput
from blocks.ParameterType import ParameterType

class Constant(Block):

    family = 'Constant'
    name = 'Constant'

    def __init__(self):
        self.num = BlockParameter(
            name='constant value',
            attribute_type=ParameterType.NUMBER,
            defaultvalue=10
            # defaultvalue=''
        )
        self.output = BlockOutput(
            name='output',
            min_cardinality=1,
            max_cardinality=1,
            attribute_type=ParameterType.NUMBER
        )

    def input_params(self,data):
        self.num.set_value(int(data['constant value']))

    def execute(self):
        value = self.num.value
        self.output.set_value(value)
        return (value,'STRING')
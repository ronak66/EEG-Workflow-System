from blocks.Block import Block 
from blocks.BlockInput import BlockInput
from blocks.BlockParameter import BlockParameter
from blocks.BlockOutput import BlockOutput
from blocks.ParameterType import ParameterType

class Division(Block):

    family = 'MultiDiv'
    name = 'Division'

    def __init__(self):
        self.num1 = BlockInput(
            name='num1',
            min_cardinality=1,
            max_cardinality=1,
            attribute_type=ParameterType.NUMBER
        )
        self.num2 = BlockInput(
            name='num2',
            min_cardinality=1,
            max_cardinality=1,
            attribute_type=ParameterType.NUMBER
        )
        self.output = BlockOutput(
            name='output',
            min_cardinality=1,
            max_cardinality=1,
            attribute_type=ParameterType.NUMBER
        )
        

    def input_params(self,data):
        self.num1.set_value(int(data['num1']))
        self.num2.set_value(int(data['num2']))

    def execute(self):
        value = self.num1.value / self.num2.value
        self.output.set_value(value)
from blocks.Block import Block 
from blocks.BlockInput import BlockInput
from blocks.BlockParameter import BlockParameter
from blocks.BlockOutput import BlockOutput

class Addition(Block):

    family = 'AddSub'
    name = 'Addition'

    def input_params(self,num1,num2):
        self.num1 = BlockInput(
            name='num1',
            value=num1,
            min_cardinality=1,
            max_cardinality=1,
            input_type="int"
        )
        self.num2 = BlockInput(
            name='num2',
            value=num2,
            min_cardinality=1,
            max_cardinality=1,
            input_type="int"
        )

    def execute(self):
        value = self.num1.value + self.num2.value
        self.output = BlockOutput(
            name='output',
            value=value,
            min_cardinality=1,
            max_cardinality=1,
            output_type="int"
        )
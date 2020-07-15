from blocks.Block import Block 
from blocks.BlockInput import BlockInput
from blocks.BlockParameter import BlockParameter
from blocks.BlockOutput import BlockOutput
from blocks.ParameterType import ParameterType

import numpy as np
import matplotlib.pyplot as plt

class Plot(Block):

    family = 'Graph'
    name = 'Plot'

    def __init__(self):
        self.function = BlockParameter(
            name='function equation',
            attribute_type=ParameterType.STRING,
            defaultvalue='x'
        )
        self.graph_domain = BlockParameter(
            name='range',
            attribute_type=ParameterType.NUMBER,
            defaultvalue=100
        )

    def input_params(self,data):
        self.function.set_value(data['function equation'])
        self.graph_domain.set_value(int(data['range']))

    def execute(self):
        x = np.array(range(-self.graph_domain.value,self.graph_domain.value))
        y = eval(self.function.value)
        plt.figure()
        plt.plot(x,y)
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        plt.title('Graph Equation: {}'.format(self.function.value))
        plt.grid()
        return (None,'GRAPH')
        
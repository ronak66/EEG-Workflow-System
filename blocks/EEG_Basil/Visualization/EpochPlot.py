'''================================
Title: Epoch Plot Block
Author: Ronak Doshi (ronak66)
================================'''

from blocks.Block import Block 
from blocks.BlockInput import BlockInput
from blocks.BlockParameter import BlockParameter
from blocks.BlockOutput import BlockOutput
from blocks.ParameterType import ParameterType

import numpy as np
import matplotlib.pyplot as plt

class EpochPlot(Block):

    family = 'Visualization'
    name = 'EpochPlot'

    def __init__(self):
        self.epochs = BlockInput(
            name='Epochs',
            min_cardinality=1,
            max_cardinality=1,
            attribute_type=ParameterType.EPOCHS
        )

    def input_params(self,data):
        self.epochs.set_value(data['Epochs'])

    def execute(self):
        epochs = self.epochs.value
        plot = epochs.plot_image(picks=None, cmap='interactive', sigma=1., combine='mean', show=False)
        return (plot[0],'GRAPH')
        
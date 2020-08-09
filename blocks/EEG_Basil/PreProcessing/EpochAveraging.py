'''================================
Title: Epoch Extraction Block
Author: Ronak Doshi (ronak66)
================================'''

from blocks.Block import Block 
from blocks.BlockInput import BlockInput
from blocks.BlockParameter import BlockParameter
from blocks.BlockOutput import BlockOutput
from blocks.ParameterType import ParameterType

import os
import mne

class EpochAveraging(Block):

    family = 'PreProcessing'
    name = 'EpochAveraging'

    def __init__(self):
        self.epochs = BlockInput(
            name='Epochs',
            min_cardinality=1,
            max_cardinality=1,
            attribute_type=ParameterType.EPOCHS
        )
        self.epochs_output = BlockOutput(
            name='Epochs',
            min_cardinality=1,
            max_cardinality=100,
            attribute_type=ParameterType.EPOCHS
        )

    def input_params(self,data):
        self.epochs.set_value(data['Epochs'])

    def execute(self):
        avgepoch = self.epochs.value.average()
        self.epochs_output.set_value(avgepoch)
        return None
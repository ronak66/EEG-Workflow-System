'''================================
Title: Channel Names Block
Author: Ronak Doshi (ronak66)
================================'''

from blocks.Block import Block 
from blocks.BlockInput import BlockInput
from blocks.BlockParameter import BlockParameter
from blocks.BlockOutput import BlockOutput
from blocks.ParameterType import ParameterType

import numpy as np
import matplotlib.pyplot as plt

class ChannelNames(Block):

    family = 'PreProcessing'
    name = 'ChannelNames'

    def __init__(self):
        self.eeg_data = BlockInput(
            name='EEGData',
            min_cardinality=1,
            max_cardinality=1,
            attribute_type=ParameterType.EEGDATA
        )

    def input_params(self,data):
        self.eeg_data.set_value(data['EEGData'])

    def execute(self):
        value = self.eeg_data.value
        return (value.ch_names,'STRING')
        
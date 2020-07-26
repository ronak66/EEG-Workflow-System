'''================================
Title: Channel Selection Block
Author: Ronak Doshi (ronak66)
================================'''

from blocks.Block import Block 
from blocks.BlockInput import BlockInput
from blocks.BlockParameter import BlockParameter
from blocks.BlockOutput import BlockOutput
from blocks.ParameterType import ParameterType

import os
import mne

class ChannelSelection(Block):

    family = 'PreProcessing'
    name = 'ChannelSelection'

    def __init__(self):
        self.eeg_data = BlockInput(
            name='EEGData',
            min_cardinality=1,
            max_cardinality=1,
            attribute_type=ParameterType.NUMBER_ARRAY
        )
        self.channels = BlockParameter(
            name='Channels',
            attribute_type=ParameterType.STRING_ARRAY,
            defaultvalue='',
            description='Select channel'
        )
        self.eeg_data_output = BlockOutput(
            name='EEGData',
            min_cardinality=1,
            max_cardinality=100,
            attribute_type=ParameterType.NUMBER_ARRAY
        )

    def input_params(self,data):
        self.channels.set_value(data['Channels'])
        self.eeg_data.set_value(data['EEGData'])

    def execute(self):
        value = self.eeg_data.value
        value = value.pick_channels(self.channels.value)

        self.eeg_data_output.set_value(value)

        return (value.get_data().shape,'STRING')
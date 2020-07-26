'''================================
Title: EEG Plot Block
Author: Ronak Doshi (ronak66)
================================'''

from blocks.Block import Block 
from blocks.BlockInput import BlockInput
from blocks.BlockParameter import BlockParameter
from blocks.BlockOutput import BlockOutput
from blocks.ParameterType import ParameterType

import numpy as np
import matplotlib.pyplot as plt

class EEGPlot(Block):

    family = 'Visualization'
    name = 'EEGPlot'

    def __init__(self):
        self.eeg_data = BlockInput(
            name='EEGData',
            min_cardinality=1,
            max_cardinality=1,
            attribute_type=ParameterType.NUMBER_ARRAY
        )

    def input_params(self,data):
        self.eeg_data.set_value(data['EEGData'])

    def execute(self):
        value = self.eeg_data.value
        channels = value.ch_names   

        time = value.times
        plt.figure(figsize=(20,10)) 
        data = value.get_data()
        for i in range(data.shape[0]):
            plt.plot(time,np.array(data[i:i+1,:]).flatten())
            print(channels[i])
        plt.legend(channels)
        plt.xlabel('Time (s)')
        plt.ylabel('EEG Amplitude')
        plt.title('EEG Data of channel/s: {}'.format(value.ch_names))
        plt.grid()
        return (None,'GRAPH')
        
'''================================
Title: Data provider Block
Author: Ronak Doshi (ronak66)
================================'''

from blocks.Block import Block 
from blocks.BlockInput import BlockInput
from blocks.BlockParameter import BlockParameter
from blocks.BlockOutput import BlockOutput
from blocks.ParameterType import ParameterType

import os
import mne

class OfflineDataProvider(Block):

    family = 'DataProvider'
    name = 'OfflineDataProvider'

    def __init__(self):
        self.eeg_data = BlockParameter(
            name='EEG File',
            attribute_type=ParameterType.FILE,
            defaultvalue='',
            description='Select only the ".eeg" file, but folder must contain ".vhdr" and ".vmrk" files'
        )
        self.eeg_data_output = BlockOutput(
            name='EEGData',
            min_cardinality=1,
            max_cardinality=100,
            attribute_type=ParameterType.EEGDATA
        )

    def input_params(self,data):
        path = data['EEG File'].split('/')
        path = Block.FILE_BASE_PATH + '/' + '/'.join(path[1:])
        vhdr_path = '.'.join(path.split('.')[:-1]) + '.vhdr'
        raw =  mne.io.read_raw_brainvision(vhdr_path)
        self.eeg_data.set_value(raw)

    def execute(self):
        value = self.eeg_data.value
        value.load_data()

        self.eeg_data_output.set_value(value)
        
        return (value.get_data().shape,'STRING')
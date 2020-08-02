'''================================
Title: Filter Block
Author: Ronak Doshi (ronak66)
================================'''

from blocks.Block import Block 
from blocks.BlockInput import BlockInput
from blocks.BlockParameter import BlockParameter
from blocks.BlockOutput import BlockOutput
from blocks.ParameterType import ParameterType

import os
import mne

class Filter(Block):

    family = 'PreProcessing'
    name = 'Filter'

    def __init__(self):
        self.eeg_data = BlockInput(
            name='EEGData',
            min_cardinality=1,
            max_cardinality=1,
            attribute_type=ParameterType.EEGDATA
        )
        self.low_cutoff_freq = BlockParameter(
            name='Low Cutoff Frequency',
            attribute_type=ParameterType.NUMBER,
            defaultvalue='None',
            description='If None the data are only low-passed'
        )
        self.high_cutoff_freq = BlockParameter(
            name='High Cutoff Frequency',
            attribute_type=ParameterType.NUMBER,
            defaultvalue='None',
            description='If None the data are only high-passed'
        )
        self.eeg_data_output = BlockOutput(
            name='EEGData',
            min_cardinality=1,
            max_cardinality=100,
            attribute_type=ParameterType.EEGDATA
        )

    def input_params(self,data):
        self.eeg_data.set_value(data['EEGData'])
        if(data['Low Cutoff Frequency']=='None'):
            self.low_cutoff_freq.set_value(None)
        else:
            self.low_cutoff_freq.set_value(float(data['Low Cutoff Frequency']))
        if(data['High Cutoff Frequency']=='None'):
            self.high_cutoff_freq.set_value(None)
        else:
            self.high_cutoff_freq.set_value(float(data['High Cutoff Frequency']))

    def execute(self):
        raw = self.eeg_data.value
        raw.filter(
            self.low_cutoff_freq.value,
            self.high_cutoff_freq.value, 
            fir_design='firwin'
        )
        self.eeg_data_output.set_value(raw)
        return None
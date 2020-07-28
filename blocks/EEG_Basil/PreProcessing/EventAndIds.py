'''================================
Title: Event and Ids Block
Author: Ronak Doshi (ronak66)
================================'''

from blocks.Block import Block 
from blocks.BlockInput import BlockInput
from blocks.BlockParameter import BlockParameter
from blocks.BlockOutput import BlockOutput
from blocks.ParameterType import ParameterType

import mne
import numpy as np
import matplotlib.pyplot as plt

class EventAndIds(Block):

    family = 'PreProcessing'
    name = 'EventAndIds'
    description = "Dictionary of 'Name' : 'Id' pair"

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
        raw = self.eeg_data.value
        events, event_ids = mne.events_from_annotations(raw)
        return (event_ids,'STRING')
        
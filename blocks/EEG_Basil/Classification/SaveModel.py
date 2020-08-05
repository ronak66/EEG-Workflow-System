'''================================
Title: Save Model Block
Author: Ronak Doshi (ronak66)
================================'''

from blocks.Block import Block 
from blocks.BlockInput import BlockInput
from blocks.BlockParameter import BlockParameter
from blocks.BlockOutput import BlockOutput
from blocks.ParameterType import ParameterType

import os
import mne
import pywt
import keras
import numpy as np
from keras.layers import Dense
from keras.models import Sequential

class SaveModel(Block):

    family = 'Classification'
    name = 'SaveModel'

    def __init__(self):
        self.model = BlockInput(
            name='Model',
            min_cardinality=0,
            max_cardinality=1,
            attribute_type=ParameterType.MODEL
        )
        self.model_out = BlockOutput(
            name='Model',
            min_cardinality=1,
            max_cardinality=100,
            attribute_type=ParameterType.MODEL
        )

    def input_params(self,data):
        if('Model' not in data.keys()):
            self.model.set_value(None)
        else:
            self.model.set_value(data['Model'])
        
    def execute(self):
        self.model_out.set_value(self.model.value)
        return (self.model_out.value,'MODEL')
    
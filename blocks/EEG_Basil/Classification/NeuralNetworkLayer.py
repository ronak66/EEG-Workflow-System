'''================================
Title: Neural Network Layer Block
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
from keras.layers import Dense, Dropout
from keras.models import Sequential

class NeuralNetworkLayer(Block):

    family = 'Classification'
    name = 'NeuralNetworkLayer'

    def __init__(self):
        self.model = BlockInput(
            name='Model',
            min_cardinality=0,
            max_cardinality=1,
            attribute_type=ParameterType.MODEL
        )
        self.units = BlockParameter(
            name='Number of Units',
            attribute_type=ParameterType.NUMBER,
            defaultvalue='',
            description='Must be an Integer'
        )
        self.activation = BlockParameter(
            name='Activation Function',
            attribute_type=ParameterType.STRING,
            defaultvalue='relu',
            description="Either, 'sigmoid', 'relu', 'softmax', 'elu', 'leaky-relu', 'selu' or 'gelu'"
        )
        self.dropout = BlockParameter(
            name='Dropout',
            attribute_type=ParameterType.STRING,
            defaultvalue='0',
            description="Fraction of the input units to drop"
        )
        self.model_out = BlockOutput(
            name='Model',
            min_cardinality=1,
            max_cardinality=100,
            attribute_type=ParameterType.MODEL
        )

    def input_params(self,data):
        act_func = ['sigmoid', 'relu', 'softmax', 'elu', 'leaky-relu', 'selu', 'gelu']
        if('Model' not in data.keys()):
            self.model.set_value(None)
        else:
            self.model.set_value(data['Model'])
        self.units.set_value(int(data['Number of Units']))
        self.activation.set_value(data['Activation Function'])
        self.dropout.set_value(float(data['Dropout']))
        

    def execute(self):
        if(self.model.value==None):
            model = Sequential()
        else:
            model = self.model.value
        model.add(Dense(self.units.value, activation=self.activation.value))
        model.add(Dropout(self.dropout.value))
        self.model_out.set_value(model)

        return None
    
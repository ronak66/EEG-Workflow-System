'''================================
Title: Wavelet Transform Block
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
import numpy as np

class WaveletTransform(Block):

    family = 'FeatureExtraction'
    name = 'WaveletTransform'

    def __init__(self):
        self.epochs = BlockInput(
            name='Epochs',
            min_cardinality=1,
            max_cardinality=1,
            attribute_type=ParameterType.EPOCHS
        )
        self.feature_vector = BlockOutput(
            name='FeatureVector',
            min_cardinality=1,
            max_cardinality=100,
            attribute_type=ParameterType.FEATUREVECTOR
        )

    def input_params(self,data):
        self.epochs.set_value(data['Epochs'])

    def execute(self):
        feature_list = []
        epochs = self.epochs.value
        event_ids = epochs.event_id

        event_id_class_mp = self.event_id_to_class(event_ids)

        for event_name,event_id in event_ids.items():
            event_epochs = epochs[event_name].get_data()
            for epoch in event_epochs:
                feature_vector = self.extractFeatures(epoch,event_id_class_mp[event_id])
                feature_list.append(feature_vector)

        self.feature_vector.set_value(feature_list)

        stdout_string = '<br>Total datapoints: {} <br> No. of Features: {}'.format(
            len(feature_list),feature_list[0].features.shape
        )

        return (stdout_string,'STRING')

    def event_id_to_class(self,event_ids):
        event_id_class_mp = {}
        i=0
        for event_name,event_id in event_ids.items():
            if(event_id not in event_id_class_mp.keys()):
                event_id_class_mp[event_id] = i
                i+=1
        return event_id_class_mp

    def extractFeatures(self,epoch,event_id):
        features = np.array([])
        for channel_data in epoch:
            coff_approx, coff_detail = pywt.dwt(channel_data,'db1')
            features = np.hstack([features,coff_detail])
        norm = np.linalg.norm(features)
        feature_vector = FeatureVector(features/norm,event_id)
        return feature_vector

class FeatureVector:

    def __init__(self,features,class_id):
        self.features = features
        self.class_id = class_id

    def set_class(self,value):
        self.class_id = value
    
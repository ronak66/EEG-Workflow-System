'''================================
Title: Feature Labeling Block
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

class FeatureLabeling(Block):

    family = 'FeatureExtraction'
    name = 'FeatureLabeling'

    def __init__(self):
        self.feature_vector = BlockInput(
            name='FeatureVector',
            min_cardinality=1,
            max_cardinality=1,
            attribute_type=ParameterType.EPOCHS
        )
        self.labels = BlockParameter(
            name='Labels',
            attribute_type=ParameterType.STRING_ARRAY,
            defaultvalue='',
            description='All comma separated event ids are considered as one class.<br>Event id will not be considered if not added'
        )
        self.feature_vector_out = BlockOutput(
            name='FeatureVector',
            min_cardinality=1,
            max_cardinality=100,
            attribute_type=ParameterType.FEATUREVECTOR
        )

    def input_params(self,data):
        self.feature_vector.set_value(data['FeatureVector'])
        self.labels.set_value(data['Labels'])

    def execute(self):
        '''
        Here every comma separated event ids are assigned same class.
        For exmaple if the block parameter is:
            - [ '2,4', '3', '5,6' ]
            - So classes are assigned like:
                - event id 2 and 4 are assigned class 0
                - event id 3 is assigned class 1
                - event id 5 and 5 are assigned class 2
        '''
        event_class_mp = self.event_class_mapping()
        features = []
        for feature in self.feature_vector.value:
            class_id = feature.class_id
            if(class_id in event_class_mp.keys()):
                feature.set_class(event_class_mp[class_id])
                features.append(feature)

        self.feature_vector_out.set_value(features)
        return (event_class_mp,'STRING')


    def event_class_mapping(self):
        mapping = {}
        class_i = 0
        for label in self.labels.value:
            event_ids = [int(x) for x in label.split(',')]
            for event_id in event_ids:
                mapping[event_id] = class_i
            class_i+=1
        return mapping
                    
    
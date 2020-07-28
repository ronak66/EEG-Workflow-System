'''================================
Title: Epoch Extraction Block
Author: Ronak Doshi (ronak66)
================================'''

from blocks.Block import Block 
from blocks.BlockInput import BlockInput
from blocks.BlockParameter import BlockParameter
from blocks.BlockOutput import BlockOutput
from blocks.ParameterType import ParameterType

import os
import mne

class EpochExtraction(Block):

    family = 'PreProcessing'
    name = 'EpochExtraction'

    def __init__(self):
        self.eeg_data = BlockInput(
            name='EEGData',
            min_cardinality=1,
            max_cardinality=1,
            attribute_type=ParameterType.NUMBER_ARRAY
        )
        self.pre_stimulus_onset = BlockParameter(
            name='PreStimulus onset',
            attribute_type=ParameterType.NUMBER,
            defaultvalue='-0.2',
            description=''
        )
        self.post_stimulus_onset = BlockParameter(
            name='PostStimulus onset',
            attribute_type=ParameterType.NUMBER,
            defaultvalue='0.5',
            description=''
        )
        self.baseline_start_time = BlockParameter(
            name='Baseline Correction Start Time',
            attribute_type=ParameterType.STRING,
            defaultvalue='None',
            description='None means beginning of the data'
        )
        self.baseline_end_time = BlockParameter(
            name='Baseline Correction End Time',
            attribute_type=ParameterType.STRING,
            defaultvalue='0',
            description='None means end of the data'
        )
        self.event_id = BlockParameter(
            name='Event Id',
            attribute_type=ParameterType.STRING,
            defaultvalue='None',
            description='None means all the events'
        )
        self.eeg_data_output = BlockOutput(
            name='EEGData',
            min_cardinality=1,
            max_cardinality=100,
            attribute_type=ParameterType.NUMBER_ARRAY
        )

    def input_params(self,data):
        self.eeg_data.set_value(data['EEGData'])
        self.pre_stimulus_onset.set_value(float(data['PreStimulus onset']))
        self.post_stimulus_onset.set_value(float(data['PostStimulus onset']))
        if(data['Baseline Correction Start Time']=='None'):
            self.baseline_start_time.set_value(None)
        else:
            self.baseline_start_time.set_value(float(data['Baseline Correction Start Time']))
        if(data['Baseline Correction End Time']=='None'):
            self.baseline_end_time.set_value(None)
        else:
            self.baseline_end_time.set_value(float(data['Baseline Correction End Time']))
        if(data['Event Id']=='None'):
            self.event_id.set_value(None)
        else:
            self.event_id.set_value(int(data['Event Id']))    

    def execute(self):
        raw = self.eeg_data.value
        events, event_id = mne.events_from_annotations(raw)

        # https://mne.tools/stable/generated/mne.Epochs.html
        epochs = mne.Epochs(
            raw, events, 
            event_id=self.event_id.value, 
            tmin=self.pre_stimulus_onset.value, 
            tmax=self.post_stimulus_onset.value, 
            baseline=(self.baseline_start_time.value, self.baseline_end_time.value), 
            preload=True
        )

        self.eeg_data_output.set_value(epochs)

        return (epochs.get_data().shape,'STRING')
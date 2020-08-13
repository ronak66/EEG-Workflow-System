'''================================
Title: Neural Network Classifier Block
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
from sklearn.model_selection import train_test_split

class NeuralNetworkClassifier(Block):

    family = 'Classification'
    name = 'NeuralNetworkClassifier'

    def __init__(self):
        self.model = BlockInput(
            name='Model',
            min_cardinality=0,
            max_cardinality=1,
            attribute_type=ParameterType.MODEL
        )
        self.feature_vector = BlockInput(
            name='FeatureVector',
            min_cardinality=0,
            max_cardinality=1,
            attribute_type=ParameterType.FEATUREVECTOR
        )
        self.optimizer = BlockParameter(
            name='Optimizer',
            attribute_type=ParameterType.STRING,
            defaultvalue='adam',
            description="Either, 'adam', 'adagrad', 'rmsprop'"
        )
        self.test_size = BlockParameter(
            name='Test Size',
            attribute_type=ParameterType.NUMBER,
            defaultvalue='0.33',
            description="Test Train Split. Ratio of test size"
        )
        self.epochs = BlockParameter(
            name='Number of Epochs',
            attribute_type=ParameterType.NUMBER,
            defaultvalue='100',
            description=""
        )
        self.classes = BlockParameter(
            name='Number of Classes',
            attribute_type=ParameterType.NUMBER,
            defaultvalue='',
            description="Number of Classification classes"
        )
        self.model_out = BlockOutput(
            name='Model',
            min_cardinality=1,
            max_cardinality=100,
            attribute_type=ParameterType.MODEL
        )

    def input_params(self,data):
        self.model.set_value(data['Model'])
        self.feature_vector.set_value(data['FeatureVector'])
        self.optimizer.set_value(data['Optimizer'])
        self.test_size.set_value(float(data['Test Size']))
        self.epochs.set_value(int(data['Number of Epochs']))
        self.classes.set_value(int(data['Number of Classes']))

    def execute(self):
        model = self.model.value
        model.compile(
            loss='categorical_crossentropy', 
            optimizer=self.optimizer.value, 
            metrics=['accuracy']
        )
        X = []
        Y = []
        for datapoint in self.feature_vector.value:
            X.append(datapoint.features)
            Y.append(datapoint.class_id)
        
        X_train, X_test, y_train, y_test = train_test_split(
            np.array(X), np.array(Y), 
            test_size=self.test_size.value, 
            random_state=42
        )
        number_of_training_sample = X_train.shape

        print(number_of_training_sample)
        print(X_test.shape)
        print(set(y_train))
        print(set(y_test))

        y_train = keras.utils.to_categorical(y_train,self.classes.value)
        y_test = keras.utils.to_categorical(y_test,self.classes.value)

        # X_train = X_test = np.array(X)
        # y_test = y_train = keras.utils.to_categorical(np.array(Y),self.classes.value)

        history = model.fit(
	    	X_train, y_train,
    		epochs=self.epochs.value,
		    validation_data=(X_test, y_test)
	    )

        self.model_out.set_value(model)

        validation_acc = history.history['val_accuracy'][-1]
        training_acc = history.history['accuracy'][-1]
        stdout = "<br>Training Accuracy: {}<br>Validation Accuracy: {}<br>No. of Training Samples: {}".format(
            training_acc,validation_acc,number_of_training_sample[0])

        return (stdout,'STRING')
    
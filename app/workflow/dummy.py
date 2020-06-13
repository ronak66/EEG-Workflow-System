a = [
    {
        "owner": "guest@guest.com",
        "public": False,
        "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
        "name": "EEGDataTable",
        "description": "",
        "family": "Visualization",
        "fields": [{
            "name": "EEGData",
            "type": "EEGDataList",
            "card": "1-2",
            "attrs": "input"
        }]
    },
    {
        "owner": "guest@guest.com",
        "public": False,
        "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
        "name": "FeatureLabelingBlock",
        "description": "",
        "family": "FeatureExtraction",
        "fields": [
            {
                "name": "Markers",
                "type": "EEGMarker[]",
                "card": "*-*",
                "attrs": "input"
            },
            {
                "name": "FeatureVectors",
                "type": "List<FeatureVector>",
                "card": "1-1",
                "attrs": "input"
            },
            {
                "name": "FeatureVectors",
                "type": "List<FeatureVector>",
                "card": "*-*",
                "attrs": "output"
            }
        ]
    },
    {
        "owner": "guest@guest.com",
        "public": False,
        "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
        "name": "OffLineDataProvider",
        "description": "",
        "family": "DataProvider",
        "fields": [
            {
                "defaultValue": "",
                "name": "EEG File",
                "description": "",
                "type": "FILE[]",
                "attrs": "editable"
            },
            {
                "name": "EEGData",
                "type": "EEGDataList",
                "card": "*-*",
                "attrs": "output"
            }
        ]
    },
    {
        "owner": "guest@guest.com",
        "public": False,
        "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
        "name": "NeuralNetworkLayer",
        "description": "",
        "family": "classification",
        "fields": [
            {
                "defaultValue": "",
                "name": "NumberOfOutputs",
                "description": "",
                "type": "NUMBER",
                "attrs": "editable"
            },
            {
                "defaultValue": "",
                "name": "ActivationFunction",
                "description": "",
                "type": "java.lang.String",
                "attrs": "editable"
            },
            {
                "defaultValue": "",
                "name": "LayerType",
                "description": "",
                "type": "java.lang.String",
                "attrs": "editable"
            },
            {
                "defaultValue": "",
                "name": "LossFunction",
                "description": "",
                "type": "java.lang.String",
                "attrs": "editable"
            },
            {
                "defaultValue": "",
                "name": "NumberOfInputs",
                "description": "",
                "type": "NUMBER",
                "attrs": "editable"
            },
            {
                "defaultValue": "",
                "name": "DropOut",
                "description": "",
                "type": "NUMBER",
                "attrs": "editable"
            },
            {
                "name": "LayerChain",
                "type": "NeuralNetworkLayerChain",
                "card": "1-1",
                "attrs": "input"
            },
            {
                "name": "LayerChain",
                "type": "NeuralNetworkLayerChain",
                "card": "*-*",
                "attrs": "output"
            }
        ]
    },
    {
        "owner": "guest@guest.com",
        "public": False,
        "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
        "name": "NeuralNetClassifier",
        "description": "",
        "family": "Classification",
        "fields": [
            {
                "name": "TrainingFeatureVectors",
                "type": "List<FeatureVector>",
                "card": "1-1",
                "attrs": "input"
            },
            {
                "name": "Markers",
                "type": "EEGMarker[]",
                "card": "*-*",
                "attrs": "input"
            },
            {
                "name": "TestingFeatureVectors",
                "type": "List<FeatureVector>",
                "card": "1-1",
                "attrs": "input"
            },
            {
                "name": "Layers",
                "type": "NeuralNetworkLayerChain",
                "card": "1-1",
                "attrs": "input"
            }
        ]
    },
    {
        "owner": "guest@guest.com",
        "public": False,
        "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
        "name": "FilterBlock",
        "description": "",
        "family": "Preprocessing",
        "fields": [
            {
                "defaultValue": "1",
                "name": "Lower cutoff frequency",
                "description": "",
                "type": "NUMBER",
                "attrs": "editable"
            },
            {
                "defaultValue": "30",
                "name": "High cutoff frequency",
                "description": "",
                "type": "NUMBER",
                "attrs": "editable"
            },
            {
                "name": "EEGData",
                "type": "EEGDataList",
                "card": "1-1",
                "attrs": "input"
            },
            {
                "name": "EEGData",
                "type": "EEGDataList",
                "card": "*-*",
                "attrs": "output"
            }
        ]
    },
    {
        "owner": "guest@guest.com",
        "public": False,
        "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
        "name": "EpochExtraction",
        "description": "",
        "family": "Preprocessing",
        "fields": [
            {
                "defaultValue": "0",
                "name": "PreStimulus onset",
                "description": "",
                "type": "NUMBER",
                "attrs": "editable"
            },
            {
                "defaultValue": "0",
                "name": "PostStimulus onset",
                "description": "",
                "type": "NUMBER",
                "attrs": "editable"
            },
            {
                "name": "EEGData",
                "type": "EEGDataList",
                "card": "1-1",
                "attrs": "input"
            },
            {
                "name": "EEGData",
                "type": "EEGDataList",
                "card": "*-*",
                "attrs": "output"
            }
        ]
    },
    {
        "owner": "guest@guest.com",
        "public": False,
        "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
        "name": "EEGMarkerBlock",
        "description": "",
        "family": "Preprocessing",
        "fields": [
            {
                "defaultValue": "",
                "name": "Name",
                "description": "",
                "type": "STRING",
                "attrs": "editable"
            },
            {
                "defaultValue": "0",
                "name": "Offset",
                "description": "",
                "type": "NUMBER",
                "attrs": "editable"
            },
            {
                "name": "marker",
                "type": "EEGMarker",
                "card": "*-*",
                "attrs": "output"
            }
        ]
    },
    {
        "owner": "guest@guest.com",
        "public": False,
        "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
        "name": "ChannelSelection",
        "description": "",
        "family": "Preprocessing",
        "fields": [
            {
                "defaultValue": "",
                "name": "channels",
                "description": "",
                "type": "STRING[]",
                "attrs": "editable"
            },
            {
                "name": "EEGData",
                "type": "EEGDataList",
                "card": "1-1",
                "attrs": "input"
            },
            {
                "name": "EEGData",
                "type": "EEGDataList",
                "card": "*-*",
                "attrs": "output"
            }
        ]
    },
    {
        "owner": "guest@guest.com",
        "public": False,
        "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
        "name": "XdfDataProvider",
        "description": "",
        "family": "DataProvider",
        "fields": [
            {
                "defaultValue": "",
                "name": "XDF File",
                "description": "",
                "type": "FILE[]",
                "attrs": "editable"
            },
            {
                "defaultValue": "",
                "name": "EEG Stream Name",
                "description": "",
                "type": "STRING",
                "attrs": "editable"
            },
            {
                "defaultValue": "",
                "name": "Marker Stream Name",
                "description": "",
                "type": "STRING",
                "attrs": "editable"
            },
            {
                "name": "EEGData",
                "type": "EEGDataList",
                "card": "*-*",
                "attrs": "output"
            }
        ]
    },
    {
        "owner": "guest@guest.com",
        "public": False,
        "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
        "name": "LSLOutput",
        "description": "",
        "family": "DataProvider",
        "fields": [{
            "name": "EEGData",
            "type": "EEGDataList",
            "card": "1-1",
            "attrs": "input"
        }]
    },
    {
        "owner": "guest@guest.com",
        "public": False,
        "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
        "name": "WaveletTransformBlock",
        "description": "",
        "family": "FeatureExtraction",
        "fields": [
            {
                "name": "EEGData",
                "type": "EEGDataList",
                "card": "1-1",
                "attrs": "input"
            },
            {
                "name": "FeatureVectors",
                "type": "List<FeatureVector>",
                "card": "*-*",
                "attrs": "output"
            }
        ]
    },
    {
        "owner": "guest@guest.com",
        "public": False,
        "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
        "name": "AveragingBlock",
        "description": "",
        "family": "Preprocessing",
        "fields": [
            {
                "name": "EEGData",
                "type": "EEGDataList",
                "card": "1-1",
                "attrs": "input"
            },
            {
                "name": "Markers",
                "type": "EEGMarker[]",
                "card": "*-*",
                "attrs": "input"
            },
            {
                "name": "EEGData",
                "type": "EEGDataList",
                "card": "*-*",
                "attrs": "output"
            }
        ]
    },
    {
        "owner": "guest@guest.com",
        "public": False,
        "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
        "name": "IntervalSelectionBlock",
        "description": "",
        "family": "Preprocessing",
        "fields": [
            {
                "defaultValue": "512",
                "name": "Samples",
                "description": "",
                "type": "NUMBER",
                "attrs": "editable"
            },
            {
                "defaultValue": "200",
                "name": "Start index",
                "description": "",
                "type": "NUMBER",
                "attrs": "editable"
            },
            {
                "name": "EEGData",
                "type": "EEGDataList",
                "card": "1-1",
                "attrs": "input"
            },
            {
                "name": "EEGData",
                "type": "EEGDataList",
                "card": "*-*",
                "attrs": "output"
            }
        ]
    },
    {
        "owner": "guest@guest.com",
        "public": False,
        "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
        "name": "EEGPlot",
        "description": "",
        "family": "Visualization",
        "fields": [{
            "name": "EEGData",
            "type": "EEGDataList",
            "card": "1-1",
            "attrs": "input"
        }]
    },
    {
        "owner": "guest@guest.com",
        "public": False,
        "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
        "name": "LSLDataProvider",
        "description": "",
        "family": "DataProvider",
        "fields": [
            {
                "defaultValue": "",
                "name": "Buffer size",
                "description": "",
                "type": "NUMBER",
                "attrs": "editable"
            },
            {
                "name": "EEGData",
                "type": "EEGDataList",
                "card": "*-*",
                "attrs": "output"
            }
        ]
    },
    {
        "owner": "guest@guest.com",
        "public": False,
        "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
        "name": "BaselineCorrection",
        "description": "",
        "family": "Preprocessing",
        "fields": [
            {
                "defaultValue": "",
                "name": "EndTime",
                "description": "",
                "type": "NUMBER",
                "attrs": "editable"
            },
            {
                "defaultValue": "",
                "name": "StartTime",
                "description": "",
                "type": "NUMBER",
                "attrs": "editable"
            },
            {
                "name": "EEGData",
                "type": "EEGDataList",
                "card": "1-1",
                "attrs": "input"
            },
            {
                "name": "EEGData",
                "type": "EEGDataList",
                "card": "*-*",
                "attrs": "output"
            }
        ]
    }
]


b = [
    {
        "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
        "name": "EEGDataTable",
        "description": "",
        "family": "Visualization",
        "fields": [
            {
                "name": "EEGData",
                "type": "EEGDataList",
                "card": "1-1",
                "attrs": "input"
            }
        ]
    },
    {
        "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
        "name": "WaveletTransformBlock",
        "description": "",
        "family": "FeatureExtraction",
        "fields": [
            {
                "name": "EEGData",
                "type": "EEGDataList",
                "card": "1-1",
                "attrs": "input"
            },
            {
                "name": "FeatureVectors",
                "type": "List<FeatureVector>",
                "card": "*-*",
                "attrs": "output"
            }
        ]
    },
    {
        "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
        "name": "FilterBlock",
        "description": "",
        "family": "Preprocessing",
        "fields": [
            {
                "defaultValue": "1",
                "name": "Lower cutoff frequency",
                "description": "",
                "type": "NUMBER",
                "attrs": "editable"
            },
            {
                "defaultValue": "30",
                "name": "High cutoff frequency",
                "description": "",
                "type": "NUMBER",
                "attrs": "editable"
            },
            {
                "name": "EEGData",
                "type": "EEGDataList",
                "card": "1-1",
                "attrs": "input"
            },
            {
                "name": "EEGData",
                "type": "EEGDataList",
                "card": "*-*",
                "attrs": "output"
            }
        ]
    }
]
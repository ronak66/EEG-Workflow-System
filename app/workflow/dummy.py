import json
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

c = json.dumps({
        "workflow": {
            "blocks": [
                {
                    "stdout": "13:47:39.626 [main] DEBUG org.reflections.Reflections - going to scan these urls:\njar:file:/home/ronak/.workflow_designer_files/uploadedFiles/basil_bci-1.2.0-jar-with-dependencies.jar!/\n13:47:39.806 [main] INFO  org.reflections.Reflections - Reflections took 176 ms to scan 1 urls, producing 12 keys and 63 values \n",
                    "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
                    "values": {"EEG File": ["Shared/LED_28_06_2012_104.eeg"]},
                    "x": -461.5000061035156,
                    "y": -163,
                    "id": 1,
                    "completed": True,
                    "type": "OffLineDataProvider",
                    "error": False,
                    "stderr": ""
                },
                {
                    "stdout": "13:47:44.915 [main] DEBUG org.reflections.Reflections - going to scan these urls:\njar:file:/home/ronak/.workflow_designer_files/uploadedFiles/basil_bci-1.2.0-jar-with-dependencies.jar!/\n13:47:45.080 [main] INFO  org.reflections.Reflections - Reflections took 160 ms to scan 1 urls, producing 12 keys and 63 values \n",
                    "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
                    "values": {
                        "Lower cutoff frequency": "1",
                        "High cutoff frequency": "30"
                    },
                    "x": -168.5000061035156,
                    "y": -157,
                    "id": 2,
                    "completed": True,
                    "type": "FilterBlock",
                    "error": False,
                    "stderr": ""
                },
                {
                    "stdout": "13:47:47.341 [main] DEBUG org.reflections.Reflections - going to scan these urls:\njar:file:/home/ronak/.workflow_designer_files/uploadedFiles/basil_bci-1.2.0-jar-with-dependencies.jar!/\n13:47:47.511 [main] INFO  org.reflections.Reflections - Reflections took 165 ms to scan 1 urls, producing 12 keys and 63 values \n",
                    "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
                    "values": {"channels": [""]},
                    "x": 50.4999938964844,
                    "y": -140,
                    "id": 5,
                    "completed": True,
                    "type": "ChannelSelection",
                    "error": False,
                    "stderr": ""
                }
            ],
            "edges": [
                {
                    "connector1": [
                        "EEGData",
                        "output"
                    ],
                    "connector2": [
                        "EEGData",
                        "input" 
                    ],
                    "block1": 1,
                    "block2": 2,
                    "id": 1
                },
                {
                    "connector1": [
                        "EEGData",
                        "output"
                    ],
                    "connector2": [
                        "EEGData",
                        "input"
                    ],
                    "block1": 2,
                    "block2": 5,
                    "id": 2
                }
            ]
        },
        "executionStatus": [
            {
                "stdout": "13:47:39.626 [main] DEBUG org.reflections.Reflections - going to scan these urls:\njar:file:/home/ronak/.workflow_designer_files/uploadedFiles/basil_bci-1.2.0-jar-with-dependencies.jar!/\n13:47:39.806 [main] INFO  org.reflections.Reflections - Reflections took 176 ms to scan 1 urls, producing 12 keys and 63 values \n",
                "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
                "values": {"EEG File": ["Shared/LED_28_06_2012_104.eeg"]},
                "x": -461.5000061035156,
                "y": -163,
                "id": 1,
                "completed": True,
                "type": "OffLineDataProvider",
                "error": False,
                "stderr": ""
            },
            {
                "stdout": "13:47:44.915 [main] DEBUG org.reflections.Reflections - going to scan these urls:\njar:file:/home/ronak/.workflow_designer_files/uploadedFiles/basil_bci-1.2.0-jar-with-dependencies.jar!/\n13:47:45.080 [main] INFO  org.reflections.Reflections - Reflections took 160 ms to scan 1 urls, producing 12 keys and 63 values \n",
                "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
                "values": {
                    "Lower cutoff frequency": "1",
                    "High cutoff frequency": "30"
                },
                "x": -168.5000061035156,
                "y": -157,
                "id": 2,
                "completed": True,
                "type": "FilterBlock",
                "error": False,
                "stderr": ""
            },
            {
                "stdout": "13:47:47.341 [main] DEBUG org.reflections.Reflections - going to scan these urls:\njar:file:/home/ronak/.workflow_designer_files/uploadedFiles/basil_bci-1.2.0-jar-with-dependencies.jar!/\n13:47:47.511 [main] INFO  org.reflections.Reflections - Reflections took 165 ms to scan 1 urls, producing 12 keys and 63 values \n",
                "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
                "values": {"channels": [""]},
                "x": 50.4999938964844,
                "y": -140,
                "id": 5,
                "completed": True,
                "type": "ChannelSelection",
                "error": False,
                "stderr": ""
            }
        ],
        "startTime": "2/6/20 1:47 PM",
        "id": 37,
        "endTime": "2/6/20 1:47 PM",
        "status": "COMPLETED"
    }
)
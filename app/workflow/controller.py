import json
from flask import Response, make_response, jsonify

def jar_upload():
    json_format = json.dumps(
        [
            {
                "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
                "name": "EEGDataTable",
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
        ]
    )
    return json_format


def tree_initialization():
    json_format = json.dumps(
        [
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
                    "card": "1-1",
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
            }
        ]
    )
    return json_format
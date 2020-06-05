import json
from flask import Response, make_response, jsonify

from app.user.auth import Auth
from app.workflow.dummy import a

@Auth.auth_required
def jar_upload(data):
    json_format = json.dumps(
        [
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
    )
    return json_format

@Auth.auth_required
def tree_initialization():
    # json_format = json.dumps(
    #     [
    #         {
    #             "owner": "guest@guest.com",
    #             "public": False,
    #             "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
    #             "name": "EEGDataTable",
    #             "description": "",
    #             "family": "Visualization",
    #             "fields": [{
    #                 "name": "EEGData",
    #                 "type": "EEGDataList",
    #                 "card": "1-1",
    #                 "attrs": "input"
    #             }]
    #         },
    #         {
    #             "owner": "guest@guest.com",
    #             "public": False,
    #             "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
    #             "name": "FeatureLabelingBlock",
    #             "description": "",
    #             "family": "FeatureExtraction",
    #             "fields": [
    #                 {
    #                     "name": "Markers",
    #                     "type": "EEGMarker[]",
    #                     "card": "*-*",
    #                     "attrs": "input"
    #                 },
    #                 {
    #                     "name": "FeatureVectors",
    #                     "type": "List<FeatureVector>",
    #                     "card": "1-1",
    #                     "attrs": "input"
    #                 },
    #                 {
    #                     "name": "FeatureVectors",
    #                     "type": "List<FeatureVector>",
    #                     "card": "*-*",
    #                     "attrs": "output"
    #                 }
    #             ]
    #         },
    #         {
    #             "owner": "guest@guest.com",
    #             "public": False,
    #             "module": "basil_bci-1.2.0-jar-with-dependencies.jar:cz.zcu.kiv.eeg.basil",
    #             "name": "FilterBlock",
    #             "description": "",
    #             "family": "Preprocessing",
    #             "fields": [
    #                 {
    #                     "defaultValue": "1",
    #                     "name": "Lower cutoff frequency",
    #                     "description": "",
    #                     "type": "NUMBER",
    #                     "attrs": "editable"
    #                 },
    #                 {
    #                     "defaultValue": "30",
    #                     "name": "High cutoff frequency",
    #                     "description": "",
    #                     "type": "NUMBER",
    #                     "attrs": "editable"
    #                 },
    #                 {
    #                     "name": "EEGData",
    #                     "type": "EEGDataList",
    #                     "card": "1-1",
    #                     "attrs": "input"
    #                 },
    #                 {
    #                     "name": "EEGData",
    #                     "type": "EEGDataList",
    #                     "card": "*-*",
    #                     "attrs": "output"
    #                 }
    #             ]
    #         }
    #     ]
    # )
    json_format = json.dumps(a)
    return json_format


@Auth.auth_required
def schedule_new_job(data):
    return str(37)


@Auth.auth_required
def get_all_scheduled_jobs():
    json_format = json.dumps(
        [
            {
                "startTime": "2/6/20 1:36 PM",
                "id": 36,
                "endTime": "2/6/20 1:36 PM",
                "status": "COMPLETED"
            },
            {
                "startTime": "2/6/20 1:35 PM",
                "id": 35,
                "endTime": "",
                "status": "FAILED"
            },
            {
                "startTime": "2/6/20 1:32 PM",
                "id": 34,
                "endTime": "",
                "status": "FAILED"
            }
        ]
    )
    return json_format

@Auth.auth_required
def get_job_details(data):
    # print("/"*80,data['jobId'])
    json_format = json.dumps({
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
    return json_format

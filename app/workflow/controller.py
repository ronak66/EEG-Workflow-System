import os
import json
import zipfile
import importlib
from flask import Response, make_response, jsonify, g

from app.user.auth import Auth
from app.workflow.model import Job
from app.workflow.Graph import Graph
from app.workflow.dummy import a, b

@Auth.auth_required
def jar_upload(data,files):
    try:
        print('-'*80,'Jar Upload',sep='\n')
        print(files['file'].filename)
        archive = zipfile.ZipFile(files['file'])
        old_modules = [name for name in os.listdir('blocks') if os.path.isdir(os.path.join('blocks', name)) and name != '__pycache__' ]
        new_modules = {item.split('/')[0] for item in archive.namelist()}
        for new_module in new_modules:
            if new_module in old_modules:
                return Response(
                    mimetype="application/json",
                    response=json.dumps(
                        {'error': 'Module name \'{}\' in {} already exsists, pls change the name'.\
                            format(new_module,files['file'].filename)}
                    ),
                    status=403
                )
        archive.extractall('blocks/')
        num_of_new_blocks = 0
        for new_module in new_modules:
            mapping = importlib.import_module('blocks.{}'.format(new_module))
            try:
                mp = mapping.string_classobject_mapping
            except:
                continue
            num_of_new_blocks += len(mp.keys())

        # for module in modules:
        #     for file in archive.namelist():
        #         if(file.startswith(module)):
        #             archive.extract(file, 'blocks/')
        #     os.rename('blocks/{}'.format(module),'blocks/{}:{}'.format(files['file'].filename,module))
        
        # json_format = json.dumps(b)
        # return json_format
        return Response(
            mimetype="application/json",
            response=json.dumps({'new_blocks_length': num_of_new_blocks}),
            status=200
        )
        # return str(num_of_new_blocks)

    except Exception as e:
        return Response(
            mimetype="application/json",
            response=json.dumps({'error': str(e)}),
            status=400
        )


@Auth.auth_required
def tree_initialization():
    try:
        print('-'*80,'Tree Initialisation',sep='\n')
        modules = [name for name in os.listdir('blocks') if \
            os.path.isdir(os.path.join('blocks', name)) and name != '__pycache__' ]
        block_list = []
        # module_blocks_mapping = {}
        for module in modules:
            mapping = importlib.import_module('blocks.{}'.format(module))
            # module_blocks_mapping[module] = mapping.string_classobject_mapping
            try:
                mp = mapping.string_classobject_mapping
            except:
                continue
            for key, value in mp.items():
                block_details = {
                    "owner": "guest@guest.com",
                    "public": False,
                    "module": "{}.zip:{}".format(module,module),
                    # "module": module,
                    "name": key,
                    "description": "",
                    "family": value.family,
                    "fields": generate_attribute_list(vars(value))       
                }
                block_list.append(block_details)

        # json_format = json.dumps(a)
        # return json_format
        return Response(
            mimetype="application/json",
            response=json.dumps(block_list),
            status=200
        )

    except Exception as e:
        return Response(
            mimetype="application/json",
            response=json.dumps({'error': str(e)}),
            status=400
        )


def generate_attribute_list(attributes):
    try:
        attribute_list = []
        for _, attribute in attributes.items():
            attribute_details = {
                "name": attribute.name,
                "type": attribute.attribute_type,
            }
            if(attribute.__class__.__name__ == 'BlockInput'):
                attribute_details["card"] = "{}-{}".format(attribute.min_cardinality,attribute.max_cardinality)
                attribute_details["attrs"] = "input"
            elif(attribute.__class__.__name__ == 'BlockOutput'):
                attribute_details["card"] = "{}-{}".format(attribute.min_cardinality,attribute.max_cardinality)
                attribute_details["attrs"] = "output"
            elif(attribute.__class__.__name__ == 'BlockParameter'):
                attribute_details["defaultValue"] = attribute.value
                attribute_details["description"] = ""
                attribute_details["attrs"] = "editable"
            attribute_list.append(attribute_details)
        return attribute_list 

    except Exception as e:
        return Response(
            mimetype="application/json",
            response=json.dumps({'error': str(e)}),
            status=400
        )

@Auth.auth_required
def schedule_new_job(data):
    print('-'*80,'Scheduling Job',sep='\n')
    modules = [name for name in os.listdir('blocks') if \
        os.path.isdir(os.path.join('blocks', name)) and name != '__pycache__' ]
    module_blocks_mapping = {}
    for module in modules:
        mapping = importlib.import_module('blocks.{}'.format(module))
        module_blocks_mapping[module] = mapping.string_classobject_mapping

    execute_scheduled_job(data,module_blocks_mapping)

    new_job = Job(
        user_id = g.user['id'],
        workflow = data     
    )
    new_job.save()
    return str(new_job.id)

def execute_scheduled_job(workflow,module_blocks_mapping):
    graph = Graph(workflow,module_blocks_mapping)
    pass


@Auth.auth_required
def get_all_scheduled_jobs():
    user_id = g.user['id']
    jobs = Job.get_jobs_via_user_id(user_id)
    job_list = []
    for job in jobs:
        job_details = {
            "startTime": str(job.start_time),
            "id": job.id,
            "endTime": str(job.end_time),
            "status": job.status
        }
        job_list.append(job_details)
    print(job_list)    

    # json_format = json.dumps(
    #     [
    #         {
    #             "startTime": "2/6/20 1:36 PM",
    #             "id": 36,
    #             "endTime": "2/6/20 1:36 PM",
    #             "status": "COMPLETED"
    #         },
    #         {
    #             "startTime": "2/6/20 1:35 PM",
    #             "id": 35,
    #             "endTime": "",
    #             "status": "FAILED"
    #         },
    #         {
    #             "startTime": "2/6/20 1:32 PM",
    #             "id": 34,
    #             "endTime": "",
    #             "status": "FAILED"
    #         }
    #     ]
    # )
    return json.dumps(job_list)

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

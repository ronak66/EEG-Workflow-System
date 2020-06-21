import os
import sys
import json
import zipfile
import importlib
from flask import Response, make_response, jsonify, g

from app import celery, app
from app.user.auth import Auth
from app.workflow.model import Job
from app.workflow.Graph import Graph
from app.workflow.dummy import a, b, c

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
                attribute_details["defaultValue"] = str(attribute.value)
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
    try:
        print('-'*80,'Scheduling Job',sep='\n')

        data = json.loads(data['workflow'])
            
        workflow = {
            'workflow': data,
            'executionStatus': data['blocks']
        }
        new_job = Job(
            user_id = g.user['id'],
            workflow = workflow     
        )
        new_job.save()

        execute_scheduled_job.delay(data,new_job.id)

        return Response(
            mimetype="application/json",
            response=json.dumps({'job_id': new_job.id}),
            status=200
        )

    except Exception as e:
        return Response(
            mimetype="application/json",
            response=json.dumps({'error': str(e)}),
            status=400
        )

@celery.task
def execute_scheduled_job(workflow,job_id):
    print("90"*20)
    sys.path.append(os.getcwd())
    with app.app_context():
        modules = [name for name in os.listdir('blocks') if \
            os.path.isdir(os.path.join('blocks', name)) and name != '__pycache__' ]
        module_blocks_mapping = {}
        for module in modules:
            mapping = importlib.import_module('blocks.{}'.format(module))
            module_blocks_mapping[module] = mapping.string_classobject_mapping
        graph = Graph(workflow,module_blocks_mapping,job_id)
        graph.bfs()
        graph.execute_workflow()

@Auth.auth_required
def get_all_scheduled_jobs():
    print('-'*80,'List of scheduled Jobs',sep='\n')
    user_id = g.user['id']
    jobs = Job.get_jobs_via_user_id(user_id)
    job_list = []
    for job in jobs:
        job_details = {
            "startTime": job.get_start_time(),
            "id": job.id,
            "endTime": job.get_end_time() if job.status == 'COMPLETED' else "",
            "status": job.status
        }
        job_list.append(job_details)
    return json.dumps(job_list)

@Auth.auth_required
def get_job_details(data):
    print('-'*80,'Getting Job details of id = {}'.format(data['jobId']),sep='\n')
    # json_format = c
    job_id = data['jobId']
    job = Job.query.get(job_id)
    details = {
        "startTime": job.get_start_time(),
        "id": job.id,
        "endTime": job.get_end_time() if job.status == 'COMPLETED' else "",
        "status": job.status
    }
    job.workflow.update(details)
    # return json_format
    return json.dumps(job.workflow)

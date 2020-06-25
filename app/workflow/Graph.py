import copy
import traceback
from queue import Queue
from datetime import datetime

from app.workflow.model import Job

class Graph:

    def __init__(self,workflow,module_blocks_mapping,job_id):
        self.workflow = workflow
        self.module_blocks_mapping = module_blocks_mapping
        self.block_id_output = {}
        self.job_id = job_id
    
    def create_block_id_mapping(self):
        self.mp_id_block = {}
        for block in self.workflow['blocks']:
            self.mp_id_block[block['id']] = {
                'type': block['type'],
                'module': block['module'],
                'values': block['values']
            }


    def create_adjacency_list(self):
        self.adjacency_list = {}
        self.transpose_adjacency_list = {}
        '''
        block1's output is connected to block2's input

        adjacency_list = {
            block1_id: [
                block2_id
            ]
        }

        transpose_adjacency_list = {
            block2_id: [
                {
                    'id': block1_id,
                    'input_name': block2_input_name,
                    'output_name': block1_output_name
                }
            ]
        }
        '''
        for edge in self.workflow['edges']:

            if 'output' in edge['connector1']:
                output_block = edge['block1']
                output_name = edge['connector1'][0]
                input_block = edge['block2']
                input_name = edge['connector2'][0]
            else:
                output_block = edge['block2']
                output_name = edge['connector2'][0]
                input_block = edge['block1']
                output_name = edge['connector1'][0]

            if(output_block in self.adjacency_list.keys()):
                self.adjacency_list[output_block].append(input_block)
            else:
                self.adjacency_list[output_block] = [input_block]

            if(input_block in self.transpose_adjacency_list.keys()):
                self.transpose_adjacency_list[input_block].append(
                    {
                        'id': output_block,
                        'output_name': output_name,
                        'input_name': input_name
                    }
                )
            else:
                self.transpose_adjacency_list[input_block] = [
                    {
                        'id': output_block,
                        'output_name': output_name,
                        'input_name': input_name
                    } 
                ]

    def bfs(self):
        self.create_adjacency_list()
        self.create_block_id_mapping()
        all_block_ids = self.mp_id_block.keys()
        staring_blocks = [i for i in all_block_ids if i not in self.transpose_adjacency_list.keys()]

        visited = {}
        for block_id in all_block_ids:
            visited[block_id] = 0

        queue = Queue()
        for block_id in staring_blocks:
            visited[block_id] = 1
            queue.put(block_id)

        self.final_queue = Queue()

        while(queue.qsize()):
            block_id = queue.get()
            self.final_queue.put(block_id)
            if(block_id in self.adjacency_list.keys()):
                for ngb_block_id in self.adjacency_list[block_id]:
                    all_input_ready_flag = 1
                    for input_id in self.transpose_adjacency_list[ngb_block_id]:
                        if(visited[input_id['id']]==0):
                            all_input_ready_flag = 0
                            break
                    if(all_input_ready_flag and visited[ngb_block_id]==0):
                        queue.put(ngb_block_id)
                        visited[ngb_block_id] = 1

    def execute_workflow(self):
        for block_id in list(self.final_queue.queue):
            block = self.mp_id_block[block_id]
            block_type = block['type']
            module = block['module']
            input_data = {}
            input_data.update(block['values'])
            module_blocks = copy.deepcopy(self.module_blocks_mapping[module.split(':')[1]])
            print('Executing block id: {}'.format(block_id))
            if(block_id not in self.transpose_adjacency_list.keys()):
                try:
                    module_blocks[block_type].input_params(input_data)
                    module_blocks[block_type].execute()
                except:
                    print('Status: FAILED')
                    e = traceback.format_exc()
                    self.update_job_status(block_id,str(e),'FAILED')
                    return str(e)
            else:
                try:
                    for input_ngb in self.transpose_adjacency_list[block_id]:
                        input_ngb_id = input_ngb['id']
                        input_ngb_output_name = input_ngb['output_name']

                        input_data[input_ngb['input_name']] = self.block_id_output[input_ngb_id][input_ngb_output_name]
                    
                    module_blocks[block_type].input_params(input_data)
                    module_blocks[block_type].execute()                    
                except:
                    print('Status: FAILED')
                    e = traceback.format_exc()
                    self.update_job_status(block_id,str(e),'FAILED')
                    return str(e)


            output = {}
            for _, attr in vars(module_blocks[block_type]).items():
                if(attr.__class__.__name__ ==  'BlockOutput'):
                    output[attr.name] = attr.value

            self.block_id_output[block_id] = output

            status = 'RUNNING'
            length = len(list(self.final_queue.queue))
            if(list(self.final_queue.queue)[length-1] == block_id):
                status = 'COMPLETED'
            self.update_job_status(block_id,output,status)
            print('Status: {}'.format(status))
            

    def update_job_status(self,block_id,msg,status):
        job = Job.query.get(self.job_id)
        workflow = copy.deepcopy(job.workflow)
        for block in workflow['executionStatus']:
            if(block['id'] == block_id):
                if(status != 'FAILED'):
                    block['output'] = {
                        'type': 'STRING',
                        'value': str(msg)
                    }
                block['completed'] = True
                if(status == 'FAILED'):
                    block['error'] = True
                    block['stderr'] = str(msg)
                else:    
                    block['error'] = False
                    block['stderr'] = ""
                break
        job.status = status
        if(status == 'COMPLETED'):
            job.end_time = datetime.utcnow()
        job.workflow = workflow
        job.commit()
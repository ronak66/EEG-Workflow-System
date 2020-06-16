class Graph:

    def __init__(self,workflow,):
        self.workflow = workflow
    
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
            block1_id: {
                block2_id,
                block2_input_name,
                block1_output_name
            }
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
                self.adjacency_list[output_block].append(
                    {
                        'id': input_block,
                        'output_name': output_name,
                        'input_name': input_name
                    }    
                )
            else:
                self.adjacency_list[output_block] = [
                    {
                        'id': input_block,
                        'output_name': output_name,
                        'input_name': input_name
                    } 
                ]
            if(input_block in self.transpose_adjacency_list.keys()):
                self.transpose_adjacency_list[input_block].append(output_block)
            else:
                self.transpose_adjacency_list[input_block] = [output_block]
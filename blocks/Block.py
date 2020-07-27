import os

class Block(object):

    family = "Default Family"
    name = "Default Name"

    FILE_BASE_PATH = '{}/EEGWorkflow/Shared'.format(os.path.expanduser('~'))

    def __init__(self):
        pass

    def input_params(self,data):
        pass

    def execute(self):
        pass
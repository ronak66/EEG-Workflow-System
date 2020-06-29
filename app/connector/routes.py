import os
import json
from flask import Blueprint, request, Response, make_response, jsonify

from app.connector.elFinder import connector
from app.connector.dummy import a

elf_connector = Blueprint('elf_connector', __name__)

@elf_connector.route("/elfinder/connector", methods=["GET","POST"])
def elfinder_connector():
    print("-"*80,"Elfinder Connector",sep='\n')
    print(request.form)
    if not request.form:
        print("yes form")
    print(dict(request.args))
    opts = {
		## required options
		# 'root': '/path/to/files', # full path to your files
		# 'URL': 'http://mydomain.tld/path/to/files' # can be absolute or relative
		# 'root': '/home/ronak/.EEGWORKFLOW',
        # 'root': '/home/ronak/.workflow_designer_files/workFiles/Shared',
        'root': '{}/.EEGWorkflow/Shared'.format(os.path.expanduser('~')),
		# 'URL': '.',
		## other options
		'debug': True
		# 'fileURL': False,  # download files using connector, no direct urls to files
		# 'dirSize': True,
		# 'dotFiles': True,
		# 'perms': {
		# 	'backup': {
		# 		'read': True,
		# 		'write': False,
		# 		'rm': False
		# 	},
		# 	'^/pics': {
		# 		'read': True,
		# 		'write': False,
		# 		'rm': False
		# 	}
		# },
		# 'uploadDeny': ['image', 'application'],
		# 'uploadAllow': ['image/png', 'image/jpeg'],
		# 'uploadOrder': ['deny', 'allow'],
		# 'disabled': ['rename', 'quicklook', 'upload'],
		# 'disabled': ['archive', 'extract'], # this will also disable archivers check
	}

    httpRequest = {
        'cmd':'open',
        # 'target':'Shared',
        'init':'1',
        'tree':'1',
    }
    elf = connector(opts)
    status, header, response = elf.run(httpRequest)
    # f = open('/home/ronak/test1.txt','w')
    # f.write(json.dumps(elf.run(response), indent=2, sort_keys=True))
    # f.close()
    # return json.dumps(a)
    return Response(
        mimetype="application/json",
        response=json.dumps(response),
        status=status
    )
import json
from flask import Blueprint, request, Response, make_response, jsonify

from app.connector.elFinder import connector

elf_connector = Blueprint('elf_connector', __name__)

@elf_connector.route("/elfinder/connector", methods=["GET","POST"])
def elfinder_connector():
    opts = {
		## required options
		# 'root': '/path/to/files', # full path to your files
		# 'URL': 'http://mydomain.tld/path/to/files' # can be absolute or relative
		# 'root': '/home/ronak/.EEGWORKFLOW',
        # 'root': '/home/ronak/.workflow_designer_files/workFiles/Shared',
        'root': '.',
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
        # 'target':'Shared_',
        'init':'1',
        'tree':'1',
    }
    elf = connector(opts)
    status, header, response = elf.run(httpRequest)
    print(response['debug'])
    f = open('/home/ronak/test1.txt','w')
    f.write(json.dumps(elf.run(response), indent=2, sort_keys=True))
    f.close()
    # return json.dumps(response)
    return Response(
        mimetype="application/json",
        response=json.dumps(response),
        status=status
    )
	# import json
    # f = open('/home/ronak/test2.txt','w')
    # f.write(json.dumps(elf.run(response), indent=2, sort_keys=True))
    # f.close()
    # list(2)
    # print(json.dumps(elf.run(response), indent=2, sort_keys=True))
    
    a = {
            "api": 2.1,
            "cwd": {
                "dirs": 0,
                "hash": "Shared_",
                "locked": 0,
                "mime": "directory",
                "name": "Shared",
                "read": 1,
                "size": 27020609,
                "ts": 1581616035,
                "volumeid": "Shared",
                "write": 1
            },
            "files": [
                {
                    "dirs": 0,
                    "hash": "Shared_",
                    "locked": 0,
                    "mime": "directory",
                    "name": "Shared",
                    "read": 1,
                    "size": 27020609,
                    "ts": 1581616035,
                    "volumeid": "Shared",
                    "write": 1
                },
                {
                    "hash": "Shared_L0xFRF8yOF8wNl8yMDEyXzEwNC5lZWc_E",
                    "locked": 0,
                    "mime": "application/oct-stream",
                    "name": "LED_28_06_2012_104.eeg",
                    "phash": "Shared_",
                    "read": 1,
                    "size": 27015720,
                    "ts": 1581615772,
                    "write": 1
                },
                {
                    "hash": "Shared_L0xFRF8yOF8wNl8yMDEyXzEwNC52aGRy",
                    "locked": 0,
                    "mime": "application/oct-stream",
                    "name": "LED_28_06_2012_104.vhdr",
                    "phash": "Shared_",
                    "read": 1,
                    "size": 4316,
                    "ts": 1581615973,
                    "write": 1
                },
                {
                    "hash": "Shared_L0xFRF8yOF8wNl8yMDEyXzEwNC52bXJr",
                    "locked": 0,
                    "mime": "application/oct-stream",
                    "name": "LED_28_06_2012_104.vmrk",
                    "phash": "Shared_",
                    "read": 1,
                    "size": 573,
                    "ts": 1581616035,
                    "write": 1
                }
            ],
            "netDrivers": [],
            "options": {
                "archivers": [],
                "copyOverwrite": 1,
                "disabled": [
                    "zipdl"
                ],
                "path": "",
                "separator": "/",
                "uploadMaxConn": "-1"
            }
        }
    return json.dumps(a)
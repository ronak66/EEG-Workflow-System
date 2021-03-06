import os
import cgi
import json
from flask import Blueprint, request, Response, make_response, jsonify, send_file

from app import FILE_BASE_PATH
from app.connector.elFinder import connector
# from app.connector.dummy import a

file_managment = Blueprint('file_managment', __name__)

@file_managment.route("/elfinder/connector", methods=["GET","POST"])
def elfinder_connector():
	print("="*80,"Elfinder Connector",sep='\n')
	print('Files:')
	print(request.files)
	opts = {
		## required options
		# 'root': '/path/to/files', # full path to your files
		# 'URL': 'http://mydomain.tld/path/to/files' # can be absolute or relative
		# 'root': '/home/ronak/.EEGWORKFLOW',
		# 'root': '/home/ronak/.workflow_designer_files/workFiles/Shared',
		'root': '{}/Shared'.format(FILE_BASE_PATH),
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
	if(request.form):
		httpRequest = dict(request.form)
		for file in request.files.getlist('upload[]'):			
			if('upload[]' in httpRequest.keys()):
				httpRequest['upload[]'][file.filename] = file
			else:
				httpRequest['upload[]'] = {
					file.filename: file
				}
			try:
				httpRequest['targets[]'] = list(httpRequest['targets[]'])
			except:
				continue
	elif(request.args):
		httpRequest = dict(request.args)
	elf = connector(opts)

	print('Commands:')
	print(httpRequest)
	status, header, response = elf.run(httpRequest)
	return Response(
		mimetype="application/json",
		response=json.dumps(response),
		status=status
	)

@file_managment.route("/api/workflow/file/<job_id>/<filename>", methods=["GET"])
def get_file(job_id,filename):
	path = '{}/Jobs/{}/{}'.format(FILE_BASE_PATH,job_id,filename)
	return send_file(path)
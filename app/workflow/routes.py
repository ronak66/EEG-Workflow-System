import json
from flask import Blueprint, request, Response, make_response, jsonify

from app.workflow.controller import jar_upload, tree_initialization, schedule_new_job, \
    get_all_scheduled_jobs, get_job_details

workflow = Blueprint('workflow', __name__)

@workflow.route("/upload", methods=["POST"])
def JAR_upload():
    try:
        return jar_upload()
    except Exception as e:
        return Response(
            mimetype="application/json",
            response=json.dumps({'error': e}),
            status=400
        )


@workflow.route("/initialize", methods=["POST"])
def initialize_tree():
    try:
        return tree_initialization()
    except Exception as e:
        return Response(
            mimetype="application/json",
            response=json.dumps({'error': e}),
            status=400
        )

@workflow.route("/schedule", methods=["GET","POST"])
def schedule():
    if(request.method == "POST"):
        try:
            data = request.form
            return schedule_new_job(data)
        except Exception as e:
            return Response(
                mimetype="application/json",
                response=json.dumps({'error': e}),
                status=400
            )
    else:
        try:
            return get_all_scheduled_jobs()
        except Exception as e:
            return Response(
                mimetype="application/json",
                response=json.dumps({'error': e}),
                status=400
            )


@workflow.route("/jobs", methods=["GET"])
def job_workflow():
    try:
        data = request.data
        return get_job_details(data)
    except Exception as e:
        return Response(
            mimetype="application/json",
            response=json.dumps({'error': e}),
            status=400
        )







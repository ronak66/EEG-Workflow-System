from flask import Blueprint, request, Response, make_response, jsonify

from app.workflow.controller import jar_upload, tree_initialization

workflow = Blueprint('workflow', __name__)

@workflow.route("/upload", methods=["POST"])
def JAR_upload():
    return jar_upload()


@workflow.route("/initialize", methods=["POST"])
def initialize_tree():
    return tree_initialization()


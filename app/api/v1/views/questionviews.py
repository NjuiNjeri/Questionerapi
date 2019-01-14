from flask import jsonify, Blueprint, request, json
from ..models.questionrecords import All_Questions
from datetime import datetime
from uuid import uuid4
from django.http import HttpResponse, HttpResponseNotFound

v1_all_questions_blueprint= Blueprint('questions', __name__, url_prefix='/api/v1')


@v1_all_questions_blueprint.route('/questions', methods=['POST'])
def post_question(id):
    data= request.get_json()
    title = data['title']
    question=data['question']


    return HttpResponse(status=201)


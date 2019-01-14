from flask import jsonify, Blueprint, request, json
from ..models.questionrecords import All_Questions
from datetime import datetime
from uuid import uuid4
from json import make_response, jsonify
from ..models.questionrecords import All_Questions

v1_all_questions_blueprint= Blueprint('questions', __name__, url_prefix='/api/v1')


@v1_all_questions_blueprint.route('meetup/<int>:id/questions', methods=['POST'])
def post_question(id):
    data= request.get_json()
    title = data['title']
    question=data['question']
    question_records = All_Questions()
    response = question_records.post_question(id, title, question)

    return make_response(jsonify({"Question record updated" : response}, 201))


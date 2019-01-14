from flask import jsonify, Blueprint, request, json, make_response
# from ..models.questionrecords import All_Questions
from datetime import datetime
from uuid import uuid4
from ..models.questionrecords import AllQuestions

v1_all_questions_blueprint= Blueprint('/questions', __name__, url_prefix='/api/v1')

question_records = AllQuestions()

@v1_all_questions_blueprint.route('/questions', methods=['POST'])
def post_question():
    data= request.get_json()
    meetupid = data['meetupid']
    title = data['title']
    question=data['question']
    response = question_records.post_question(meetupid, title, question)

    return make_response(jsonify({"Question record updated" : response})), 201


@v1_all_questions_blueprint.route('/questions', methods=['GET'])
def get_all():
    qstns =  question_records.get_all_questions()
    return jsonify(qstns)


from flask import jsonify, Blueprint, request, json
from ..models.questionrecords import All_Questions
from datetime import datetime
from uuid import uuid4

v1_all_questions_blueprint= Blueprint('questions', __name__, url_prefix='api/v1')

@v1_all_questions_blueprint.route('/questions', methods=['POST'])
def post_question():
    data= request.get_json()


from flask import jsonify, Blueprint, request, json
from ..models.meetuprecords import Meetup_records
from datetime import datetime
from uuid import uuid4

v1_meetup_blueprint = Blueprint('meetups', __name__, url_prefix='/api/v1')

meetup = Meetup_records()

@v1_meetup_blueprint.route('api/v1/meetups', methods=['GET'])
def post_question():
    return jsonify({"meetups": meetup.meetuprecords})
from flask import jsonify, Blueprint, request, json, Response, make_response
from ..models.allmeetuprecords import Meetup_records
from datetime import datetime
from uuid import uuid4


v1_meetup_blueprint = Blueprint('/allmeetups', __name__, url_prefix='/api/v1')

meetup = Meetup_records()

@v1_meetup_blueprint.route('/allmeetups', methods=['POST'])
def createmeetup():
    data= request.get_json()

    id = len(meetup.meetuprecords)+1
    'date' ='datetime.now'()
    "venue" 'venue'
    "title"'title'

    return make_response(jsonify({"Status", 201, "All Meetups Here"})), 201

    @v1_meetup_blueprint.route('/allmeetups', methods=['GET'])
    def get_all():
        meetup= Meetup_records.createMeetup()
        return jsonify(meetup), 200
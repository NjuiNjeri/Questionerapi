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
    date=datetime.now()
    venue= data['venue']
    title= data['title']

    return make_response(jsonify({"All Meetups Here" : response})), 201

    @v1_meetup_blueprint.route('/allmeetups', methods=['GET'])
    def get_all():
        meets= Meetup_records.createMeetup()
        return jsonify(meets), 201
from flask import jsonify, Blueprint, request, json, Response, make_response
from ..models.allmeetuprecords import Meetup_records
from datetime import datetime
from uuid import uuid4

v1_meetups_blueprint= Blueprint('/allmeetups', __name__, url_prefix='/api/v1')

meetups = Meetup_records()

@v1_meetups_blueprint.route('/allmeetups', methods=['POST'])
def post_meetup():
    data= request.get_json()
    id = data['meetupid']
    title = data['title']
    venue=data['venue']
    response = meetups.createMeetup(id, title, venue)

    return make_response(jsonify({"Meetup record updated" : response})), 201


@v1_meetups_blueprint.route('/allmeetups', methods=['GET'])
def get_all():
    meets =  meetups.get_meetups()
    return jsonify(meets)

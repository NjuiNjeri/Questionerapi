from flask import jsonify, Blueprint, request, json, make_response
from ..models.meetuprecords import Meetup_records
from datetime import datetime
from uuid import uuid4

v1_meetup_blueprint = Blueprint('/meetups', __name__, url_prefix='/api/v1')

meetup =Meetup_records()

@v1_meetup_blueprint.route('/meetups', methods=['POST'])
def post_meetup():
    data= request.get_json()
    meetupid = data['meetupid']
    title= data['title']
    response = meetup.meetuprecords.create_meetup(meetupid, title,)

    return make_response(jsonify({"Meetups updated" : response})), 201

# @v1_meetup_blueprint.route('/meetups', methods=['GET'])
# def get_allmeetups():
#     meets= meetup.get_meetup()
#     return jsonify(meets)
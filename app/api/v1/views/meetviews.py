from flask import Flask, Blueprint, jsonify, json, request, Response, make_response
from datetime import datetime
from uuid import uuid4
from ..models.createmeetup import CreateMeetups

v1_mymeetups_blueprint = Blueprint('/mymeetups', __name__, url_prefix='/api/v1')

meetup = CreateMeetups()

@v1_mymeetups_blueprint.route('/mymeetups', methods=['POST'])
def my_meetups():
    data= request.get_json()
    title = data['meetup_title']
    venue = data['meetup_venue']
    time = data['time']
    response = meetup.post_meetups(title, venue, time)
    print(response)

    return make_response(jsonify({"Meetup record updated" : response})), 201
    
@v1_mymeetups_blueprint.route('/mymeetups', methods=['GET'])
def get_all():
    views =  meetup.post_meetups()
    return jsonify(views)



from flask import Flask, Blueprint, jsonify, json, request, Response, make_response
from datetime import datetime
from uuid import uuid4
from ..models.createmeetup import CreateMeetups

v1_mymeetups_blueprint = Blueprint('meetups', __name__, url_prefix='/api/v1')

meetup = CreateMeetups()

@v1_mymeetups_blueprint.route('/meetups', methods=['POST'])
def post_meetups():
    data= request.get_json()
    title = data['title']
    venue = data['venue']
    meetup_time = data['meetup_time']
   
    meetups= meetup.createMeetup(title, venue, meetup_time)
    return jsonify({"status": 201, "data": meetups}),201
    
@v1_mymeetups_blueprint.route('/meetups', methods=['GET'])
def get_all():
    views =  meetup.post_meetups()
    return jsonify(views)

@v1_mymeetups_blueprint.route('/meetups/delete/<meetupid>', methods=['DELETE'])
def delete_meetup(meetupid):
    Meetup = meetup.delete_meetup(meetupid)
    return jsonify('Meetup')
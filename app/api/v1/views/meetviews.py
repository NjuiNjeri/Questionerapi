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
    time = data['time']
   
    meetups= meetup.createMeetup(title, venue, time)
    return jsonify({"status": 201, "data": meetups}),201
    
@v1_mymeetups_blueprint.route('/meetups', methods=['GET'])
def get_all():
    views =  meetup.post_meetups()
    return jsonify(views)

@v1_mymeetups_blueprint.route('/meetups/delete/<int:meetupId>', methods=['DELETE'])
def delete_meetup(meetupId):
    Meetup = meetup.delete_meetup(meetupId)
    return jsonify(Meetup)

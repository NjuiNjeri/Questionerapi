from flask import jsonify, Blueprint, request, json, Response
from ..models.allmeetuprecords import Meetup_records
from datetime import datetime
from uuid import uuid4


v1_meetup_blueprint = Blueprint('allmeetups', __name__, url_prefix='/api/v1')

meetup = Meetup_records()

@v1_meetup_blueprint.route('/allmeetups', methods=['POST'])
def post_question():
    data= request.get_json()

    meetupid = len(meetup.meetuprecords)+1
    date=datetime.now()
    venue= data['venue']
    title= data['title']

    meetup.createMeetup(meetupid, title, date, venue)
    return jsonify({
        "status": 201, "data":[
            {"title": "title", "venue":"venue", "date":"date", "tags": ["tag1", "tag2", "tag3"] }]}), 201



@v1_meetup_blueprint.route('/allmeetups', methods=['GET'])
def get_allmeetups():
    meetups= meetup.get_meetups()

    return jsonify(meetups), 200
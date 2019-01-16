from flask import Flask, Blueprint, jsonify
from app.api.v1.models.createmeetup import CreateMeetups


from ..models.createmeetup import CreateMeetups

v1_meetups_blueprint = Blueprint('meetups', __name__, url_prefix='/api/v1')

meetup = CreateMeetups()


@v1_meetups_blueprint.route('/meetups', methods=['GET'])
def mymeetups():
    
    return jsonify({"meetups": meetup.meetups}),


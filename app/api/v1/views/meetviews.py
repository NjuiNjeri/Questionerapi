from flask import Flask, Blueprint, jsonify
from app.api.v1.models.createmeetup import CreateMeetups
import datetime
import requests

from ..models.createmeetup import CreateMeetups

v1_meetups = Blueprint('meetups', __name__, url_prefix='/api/v1')

meetup = CreateMeetups()


@v1_meetups.route('/meetups', methods=['GET'])
def allMeetups():
    
    return jsonify({"meetups": meetup.meetups}), 201


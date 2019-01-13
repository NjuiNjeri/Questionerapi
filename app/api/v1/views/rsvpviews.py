from flask import Flask, Blueprint, jsonify
from app.api.v1.models.RSVPmeetup import RSVP

v1_rsvp=Blueprint('RSVP', __name__, url_prefix='/api/v1/RSVP')



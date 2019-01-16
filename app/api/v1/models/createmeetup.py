from datetime import datetime
from app.api.v1.views import meetviews
from flask import Flask, json, jsonify, abort, Response, make_response


class CreateMeetups:
    """ Creates the meetup class"""
    def __init__(self):
        self.meetups = []

    def createMeetup(self, meetupid="", meetup_date="", meetup_time= "", meetup_venue=""):
        '''creates new meetup'''
        newMeetup ={
            'meetupid': meetupid,
            'meetupdate': datetime,
            'meetuptime': meetup_time,
            'meetupvenue': meetup_venue,
         }

        self.meetups.append(newMeetup)

    def my_meetups(self):
        return self.meetups

       

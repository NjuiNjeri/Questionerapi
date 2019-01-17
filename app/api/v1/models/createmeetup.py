from datetime import datetime
from app.api.v1.views import meetviews
from flask import Flask, json, jsonify, abort, Response, make_response


class CreateMeetups():
    """ Creates the meetup class"""
    def __init__(self):
        self.meetups = []

    def createMeetup(self, meetupid="", meetup_title="", meetup_time= "", meetup_venue=""):
        '''creates new meetup'''
        newMeetup ={
            'meetupid': meetupid,
            'meetupdate': datetime,
            'meetuptime': meetup_time,
            'meetupvenue': meetup_venue,
         }

        self.meetups.append(newMeetup)
        return jsonify(self.meetups)

    def post_meetups(self):
        return self.meetups

    def delete_meetup(self, meetupId):
        """ Deletes a specific meetup record """
        Meetup = [Meetup for Meetup in self.meetups if Meetup['meetupId'] == meetupId]
        if Meetup:
            self.meetups.remove(Meetup[0])
        return abort(400, "Error: meetup {} doesn't exist!".format(meetupId))
    
       

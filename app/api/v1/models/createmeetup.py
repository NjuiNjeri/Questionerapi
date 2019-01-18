from datetime import datetime
from flask import Flask, json, jsonify, abort, Response, make_response


class CreateMeetups():
    """ Creates the meetup class"""
    def __init__(self):
        self.meetups = []

    def createMeetup(self, meetupid, meetup_title="", meetup_time= "", meetup_venue=""):
        '''creates new meetup'''
        newMeetup ={
            'meetupid': str(len(self.meetups) + 1),
            'meetup_title': meetup_title,
            'meetup_time': meetup_time,
            'meetupvenue': meetup_venue
         }

        self.meetups.append(newMeetup)
        return newMeetup

    def post_meetups(self):
        return self.meetups

    def delete_meetup(self, meetupid):
        """ Will remove any selected meetup record """
        Meetup = [Meetup for Meetup in self.meetups if Meetup ['meetupid'] == meetupid]
        if Meetup:
            self.meetups.remove(Meetup[0])
        return abort(400, "Message: Not found!")
    
       

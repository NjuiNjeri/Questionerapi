from flask import jsonify
from datetime import datetime




class Meetup_records:
    '''creates the meet up record'''
    def __init__(self, *args,):
        self.meetuprecords= []

    def createMeetup(self, meetupid="", meetup_date="", meetup_time= "", meetup_venue=""):
        '''creates new meetup'''
        newMeetup   ={
            'meetupid': meetupid,
            'meetupdate': datetime,
            'meetuptime': meetup_time,
            'meetupvenue': meetup_venue,
        
    }

        self.meetuprecords.append(newMeetup)

        return Meetup_records

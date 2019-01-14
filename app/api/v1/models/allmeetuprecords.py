from flask import jsonify
from datetime import datetime




class Meetup_records:
    '''creates the meet up record'''
    def __init__(self, *args,):
        self.meetuprecords= []

    def createMeetup(self, meetupid, date, time, venue):
        '''creates new meetup'''
        newMeetup   ={
            'meetupid': meetupid,
            'meetupdate': datetime,
            'meetuptime': time,
            'meetupvenue': venue,
        
    }

        self.meetuprecords.append(newMeetup)

        return self.meetuprecords

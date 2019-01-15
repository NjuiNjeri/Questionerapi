from flask import jsonify, abort
from datetime import datetime




class Meetup_records:
    '''creates the meet up record'''
    def __init__(self):
        self.meetuprecords= []

    def createMeetup(self, meetupid, title, date, venue):
        '''creates new meetup and adds it to the self.meetuprecords list'''

        self.meetupid= meetupid
        self.title= title
        self.date= datetime.now()
        self.venue= venue

        newMeetup   ={
            'id': meetupid,
            'date': datetime,
            'venue': venue
        
    }

        self.meetuprecords.append(newMeetup)

        return self.meetuprecords

    def get_meetups(self):
        return self.meetuprecords

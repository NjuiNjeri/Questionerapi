from flask import jsonify, abort
from datetime import datetime




class Meetup_records:
    '''creates the meet up record'''
    def __init__(self):
        self.meetuprecords= []

    def createMeetup(self, id, title, venue):
        '''creates new meetup and adds it to the self.meetuprecords list'''

        self.meetupid= id
        self.title= title
        self.date= datetime.now()
        self.venue= venue

        newMeetup   ={
            'id': id,
            'date': datetime,
            'venue': venue
        
    }

        self.meetuprecords.append(newMeetup)

        return self.meetuprecords

    def get_meetups(self):
        return self.meetuprecords

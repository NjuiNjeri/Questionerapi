from flask import jsonify, abort
from datetime import datetime





class Meetup_records:
    '''creates the meet up record'''
    def __init__(self, *args,):
        self.meetuprecords= []

    def createMeetup(self, meetupid="", meetup_date="", meetup_time= "", meetup_venue=""):
        '''creates new meetup'''
        newMeetup   ={
            'meetupid': meetup,
            'meetupdate': datetime,
            'meetuptime': meetup_time,
            'meetupvenue': meetup_venue,
        
    }

        self.meetuprecords.append(newMeetup)

        def meetup(self, meetupid):
            ''' will refer to the meetupidentifier to fetch it for the user'''
            for meetup in self.meetuprecords:
                if id== int(meetupid):
                    return meetup
                else:
                    return abort (404)                   
                    
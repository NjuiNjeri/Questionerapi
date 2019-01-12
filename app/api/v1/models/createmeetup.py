from datetime import datetime



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
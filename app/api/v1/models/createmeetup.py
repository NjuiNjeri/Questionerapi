


class CreateMeetups:
    """ Creates the meetup class"""
    def __init__(self):
        self.meetups = []
        

    def createMeetup(self, meetupId):
        newMeetup = {
            "meetupId": meetupId
        }

        self.meetups.append(newMeetup)
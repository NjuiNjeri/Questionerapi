from datetime import datetime


class All_Questions():
    
    def __init__(self, *args,):
        self.all_questions:[]

        def post_question(self, questionid="", date="", user="", meetupid="", title="", body="", votes=""):
            ''' will add a new question to the self.all_questions list'''
            self.questionid= questionid
            self.date= date
            self.user= user
            self.meetupid= meetupid
            self.title= title
            self.body= body
            self.votes= []

            new_question= {
                "questionid": questionid,
                "date": date,
                "user": user,
                "meetupid": meetupid,
                "title": title,
                "body": body,
                "votes": []                 

            }

            self.all_questions.append(new_question)    
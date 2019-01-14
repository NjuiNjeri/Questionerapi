from datetime import datetime
all_questions = []


class AllQuestions():
    
    def __init__(self, *args,):
        self.records = all_questions

        def post_question(self, meetupid, title, question):
            ''' will add a new question to the self.all_questions list'''

            new_question= {
                "questionid": len(self.all_questions)+1,
                "date": datetime.now(),
                "meetupid": meetupid,
                "title": title,
                "question": question               

            }

            self.records.append(new_question)
            return self.records    
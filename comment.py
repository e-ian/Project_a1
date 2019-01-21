from datetime import datetime

comments = []

class Comment:

    def __init__(self,message, timestamp, author):
        self.message = message
        self.timestamp = datetime.today()
        self.author = author
  
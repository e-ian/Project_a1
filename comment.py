from datetime import datetime

comments = []

class Comment:

    def __init__(self,message, timestamp, author):
        self.message = message
        self.timestamp = datetime.today()
        self.author = author

    #function for creating a comment
    def create_comment(self):
        comment = dict(
            message = self.message,
            timestamp = self.timestamp,
            author = self.author
        )
        comments.append(comment)
        return comment
  
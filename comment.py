from datetime import datetime

comments = []

class Comment:

    def __init__(self,message, author):
        self.message = message
        self.timestamp = datetime.today()
        self.author = author

    #function for creating a comment
    def create_comment(self,message, author):
        comment = dict(
            message = self.message,
            timestamp = self.timestamp,
            author = self.author
        )
        comments.append(comment)
        return comment
  
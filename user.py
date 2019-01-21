class User:
    # list to hold the user
    users = []

    # initializing the user model
    def __init__(self, name, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    # creating the user
    def register_user(self, name, username, password, role):
        user = dict(
            self.username = username
            self.password = password
            self.role = role
        )
        user('{}, {}, {}').format(username, password, role)
        users.append(user)
        return user
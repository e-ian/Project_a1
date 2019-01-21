class User:
    # list to hold the user
    users = []

    # initializing the user model
    def __init__(self, name, username, password, role):
        self.name = name
        self.username = username
        self.password = password
        self.role = role

    # creating the user
    def register_user(self, name, username, password, role):
        user = dict(
            self.name = name
            self.username = username
            self.password = password
            self.role = role
        )
        user('{}, {}, {}, {}').format(name, username, password, role)
        users.append(user)
        return user
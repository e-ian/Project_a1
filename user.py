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
    def register_user(self):
        user = dict(
            username=self.username,
            email=self.email,
            password=self.password,
            last_seen=self.last_seen,
            active=self.active
            role = self.role
        )
        # user('{}, {}, {}, {}').format(self.name, self.username, self.password, self.role)
        users.append(user)
        return user
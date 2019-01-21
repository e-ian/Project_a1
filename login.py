
def login_user(self, username, password):
        """
        Method logs in a user to their account.
        :returns:
        True for the value of is_active
        and false if logged out
        """
        for user in self.users:
            if username not in user['name']:
                return 'Sorry this user does not exist!'
            if user['username'] == username and user['password'] == password and user['role'] == role:
                user['last_seen'] = self.last_seen
                user['active'] = True
                user['role'] = user
                print('You are logged in now')
                return True
            else:
                print('Sorry wrong email or password!')
                return False

def login_user(self, username, password):
        """
        Method logs in a user to their account.
        :returns:
        True for the value of is_active
        """
        for user in self.users:
            if username not in user['username']:
                return 'Sorry this user does not exist!'

            if user['username'] == username and user['password'] == password:
                user['last_seen'] = self.last_seen
                user['active'] = True
                print('You are logged in now')
                return True

            else:
                print('Sorry wrong username or password')
                return False
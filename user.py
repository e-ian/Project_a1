"""user model"""
import re
import datetime
class User:
    # list to hold the user
    users = []

    # initializing the user model
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
        

    def validate_password(self):
        """ method to validate the password 

        :returns:
        True -if password contains all required validations
        False - if password doesnt pass the validations
        """
        upper_case = re.search(r"[A-Z]", self.password)
        lower_case = re.search(r"[a-z]", self.password)
        number = re.search(r"[0-9]", self.password)
        if not all((lower_case, upper_case, number)) or len(self.password) > 6:
            return False
        else: 
            return True

    def validate_user_name(self):
        """
        method validating username on registering a user """
        if not self.username and len(self.username) < 4:
            return False
        else:
            return True

    def validate_role(self):
        """method validating the role"""
        if not self.role and len(self.role) < 4:
            return False
        else:
            return True

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

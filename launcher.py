from user import User



if __name__=="__main__":
    username=input("Username:")
    passward =input("Password:")
    userrole =input("Role:")
    new_user = User(username, passward, userrole)
    new_user.register_user(username, passward, userrole)
    print(new_user.get_users())
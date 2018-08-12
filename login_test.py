user_names = ["cc9g15"]
passwords = ["Abcd1234"]
def login():
    user = input("enter username")
    password = input("enter password")
    if user in user_names and password == passwords[user_names.index(user)]:
        print("logged in")
    else:
        print("logged out")

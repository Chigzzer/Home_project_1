import password_generator as pg

users = []
passwords = []

def gen_login():
    user_name = input("Please enter your username")
    if user_name in users:
        print("That username is already taken, please try again")
        gen_login()
    else:
        users.append(user_name)
        want_password = input("Do you want us to generate a password for you, yes or no?")
        if want_password == "yes":
            password = pg.create_password()
            print(password)
            print("Your password is {}".format(password))
        else:
            password = input("Please enter your password")
            print("Your password is {}".format(password))

        passwords.append(password)
gen_login()
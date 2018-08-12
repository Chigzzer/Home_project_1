import random
password_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', '#']


def create_password():
    len_of_pass = input("how long do you want your password to be")
    password = []
    num = 0
    while num < int(len_of_pass):
        password.append(random.choice(password_characters))
        final_pass = ''.join(password)
        num += 1
    return final_pass

create_password()
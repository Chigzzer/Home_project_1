def translate_test():
    check = []
    input_string = input("Please input what you want to translate into english here, in lower case.")
    English_dic = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', ' ']
    trans = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                    'w', 'x', 'y', 'z', ' ']
    letter = list(input_string)
    print(letter)
    for i in letter:
        id = trans.index(i)
        translated = English_dic[id]
        check.append(translated)
    print(''.join(check))
translate_test()
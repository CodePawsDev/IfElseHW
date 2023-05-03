# check whether a character is uppercase or lowercase alphabet.
# a-z(97-122) and A-Z (65-90)

user_ans = 'y'

while user_ans.lower() == 'y':
    char = input('Enter character here: ')

    if (ord(char) >= 97 and ord(char) <= 122):
        print(f'{char} is lowercase alphabet.')
    elif (ord(char) >= 65 and ord(char) <= 90):
        print(f'{char} is uppercase alphabet.')
    else:
        print(f'{char} is not alphabet.')

    user_ans = input('\nDo you want to continue? (y/n): ')
# check whether a character is alphabet or not.
# only a-z(97-122) and A-Z (65-90)

user_ans = 'y'
while user_ans.lower() == 'y':
    char_in = input('Enter your character here: ')

    if (ord(char_in) > 64 and ord(char_in) < 91) or (ord(char_in) > 96 and ord(char_in) < 123):
        print(f'{char_in} is alphabet.')
    else:
        print(f'{char_in} is not alphabet.')

    user_ans = input('\nDo you want to continue? (y/n): ')

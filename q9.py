# input any character and check whether it is alphabet, digit or special character.
# a-z(97-122) and A-Z (65-90)
# 0-9(48-57)

user_ans = 'y'

while user_ans.lower() == 'y':
    user_input = input('Enter any character here: ')

    if (ord(user_input) >= 97 and ord(user_input) <= 122) or (ord(user_input) >= 65 and ord(user_input) <= 90):
        print(f'{user_input} is alphabet.')
    elif (ord(user_input) >= 48 and ord(user_input) <= 57):
        print(f'{user_input} is digit.')
    else:
        print(f'{user_input} is special character.')

    user_ans = input('\nDo you want to continue? (y/n): ')
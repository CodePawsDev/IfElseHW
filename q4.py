# check whether a number is divisible by 5 and 11 or not.

user_ans = 'y'

while user_ans.lower() == 'y':
    num = int(input('Enter a number: '))

    if (num % 5 == 0) and (num % 11 == 0):
        print(f'{num} can be divided by 5 and 11.')
    else:
        print(f'{num} can not be divided by 5 and 11.') 

    user_ans = input('\nDo you want to continue? (y/n): ')
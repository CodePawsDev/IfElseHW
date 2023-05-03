# check whether a number is negative, positive or zero.

user_ans = 'y'

while user_ans.lower() == 'y':
    num = int(input('Enter a number: '))
    
    if num == 0:
        print(f'{num} is zero.')
    else:
        if num > 0:
            print(f'{num} is positive.')
        else:
            print(f'{num} is negative.')

    user_ans = input('\nDo you want to continue? (y/n): ')

# check whether a number is even or odd.

user_ans = 'y'

while user_ans.lower() == 'y':
    num = int(input('Enter a number: '))
    
    if num % 2 == 0:
        print(f'{num} is even.')
    else:
        print(f'{num} is odd.')

    user_ans = input('\nDo you want to continue? (y/n): ')
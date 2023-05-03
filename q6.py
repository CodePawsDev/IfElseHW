# check whether a year is leap year or not.

user_ans = 'y'

while user_ans.lower() == 'y':
    year = int(input('Enter year: '))

    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        print(f'{year} is a leap year.')
    else:
        print(f'{year} is not a leap year.')

    user_ans = input('\nDo you want to continue? (y/n): ')
    

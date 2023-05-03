# input week number and print week day.

weekday_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

user_ans = 'y'
while user_ans.lower() == 'y':
    week_n = int(input('Enter week number (1-7): '))
    while (week_n < 1) or (week_n > 7):
        week_n = int(input('Please enter week number (1-7) again: '))
    
    print(f'{week_n} is {weekday_dict[week_n]}') # dict[key]

    user_ans = input('\nDo you want to continue? (y/n): ')


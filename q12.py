# input month number and print number of days in that month.

user_ans = 'y'

day_30 = [4,6,9,11]
day_31 = [1,3,5,7,8,10,12]

month_dict = { 1:'January', 2:'February', 3:'March', 4:'April',
              5:'May', 6:'June', 7:'July', 8:'August', 9:'September',
              10:'October', 11:'November', 12:'December'}

while user_ans.lower() == 'y':
    month_n = int(input('Enter month number: '))
    while (month_n < 1) or (month_n > 12):
        month_n = int(input('Please enter month number again (1-12): '))

    if month_n in day_30:
        print(f'{month_dict[month_n]} has 30 days.')
    elif month_n in day_31:
        print(f'{month_dict[month_n]} has 31 days.')
    else:
        print(f'{month_dict[month_n]} has 28 or 29 days.')

    user_ans = input('\nDo you want to continue? (y/n): ')
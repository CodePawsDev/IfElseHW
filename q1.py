# find maximum between two numbers.

user_ans = 'y'

while user_ans.lower() == 'y':
    first_n = int(input('Enter first number: '))
    second_n = int(input('Enter second number: '))

    if first_n > second_n:
        print(f'The maximum number is {first_n:,}.')
    elif second_n > first_n:
        print(f'The maximun number is {second_n:,}.')
    else:
        print('They are equal.')

    user_ans = input('\nDo you want to continue? (y/n): ')
    

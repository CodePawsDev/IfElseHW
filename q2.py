# find maximum between three numbers.

user_ans = 'y'

while user_ans.lower() == 'y':
    first_n = int(input('Enter first number: '))
    second_n = int(input('Enter second number: '))
    third_n = int(input('Enter third number: '))

    if (first_n == second_n) and (first_n == third_n):
        print('They are equal.')
    elif (first_n > second_n) and (first_n > third_n):
        print(f'The maximum number is {first_n}.')
    elif (second_n > first_n) and (second_n > third_n):
        print(f'The maximum number is {second_n}.')
    else:
        print(f'The maximun number is {third_n}.')

    user_ans = input('\nDo you want to continue? (y/n): ')
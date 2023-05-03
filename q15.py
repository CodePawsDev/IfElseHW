# input all sides of a triangle and check whether triangle is valid or not.

'''
A triangle is valid if sum of its two sides is greater than the third side. 
Means if a, b, c are three sides of a triangle. 
Then the triangle is valid if all three conditions are satisfied.
a + b > c
a + c > b and
b + c > a
'''

user_ans = 'y'

while user_ans.lower() == 'y':
    sides_list = []  # reset sides_list  
    for i in range(1,4):
        side = int(input(f'Enter side {i}: '))
        while side < 1:
            side = int(input(f'Please enter side {i} again: '))
        sides_list.append(side)
    


    if sides_list[0] + sides_list[1] > sides_list[2] and sides_list[0] + sides_list[2] > sides_list[1] and sides_list[1] + sides_list[2] > sides_list[0]:
        print('This is valid triangle.')
    else:
        print('No, this is invalid triangle.')

    user_ans = input('\nDo you want to continue? (y/n): ')
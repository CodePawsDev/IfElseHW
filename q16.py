# check whether the triangle is equilateral, isosceles or scalene triangle.

'''
If a, b, c are three sides of triangle. 
The triangle is equilateral only if a == b == c.
The triangle is isosceles if either a == b or a == c or b == c.
The triangle is scalene if none of its sides are equal.
'''

user_ans = 'y'

while user_ans.lower() == 'y':
    sides_list = []  # reset sides_list  
    for i in range(1,4):
        side = int(input(f'Enter side {i}: '))
        while side < 1:
            side = int(input(f'Please enter side {i} again: '))
        sides_list.append(side)
    
    if sides_list[0] == sides_list[1] == sides_list[2]:
        print('This triangle is equilateral.')
    elif sides_list[0] == sides_list[1] or  sides_list[0] == sides_list[2] or sides_list[1] == sides_list[2]:
        print('This triangle is isosceles.')
    else:
        print('This triangle is scalene.')

    user_ans = input('\nDo you want to continue? (y/n): ')

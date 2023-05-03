# input angles of a triangle and check whether triangle is valid or not.
# The sum of the three angles is always 180 degrees. 

user_ans = 'y'

while user_ans.lower() == 'y':
    angle_list = []  # reset angle_list 
    for i in range(1,4):
        angle = int(input(f'Enter angle {i}: '))
        while angle < 1:
            angle = int(input(f'Please enter angle {i} again: '))
        angle_list.append(angle)

    sum_angles = angle_list[0] + angle_list[1] + angle_list[2]

    if sum_angles == 180:
        print('This is valid triangle.')
    else:
        print('This is invalid triangle.')

    user_ans = input('\nDo you want to continue? (y/n): ')
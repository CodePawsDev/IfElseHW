'''
input marks of five subjects 
Physics, Chemistry, Biology, Mathematics and Computer. 
Calculate percentage and grade according to following:

Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% : Grade F
'''
# define function to input mark for each subject
def mark(subject):
    marks = 0
    while marks < 1 or marks > 100:
        marks = int(input(f'Enter {subject} marks (out of 100): '))
    return marks

user_ans = 'y'

while user_ans.lower() == 'y':
    phys = mark('physics') # function call
    chem = mark('chemistry')
    bio = mark('biology')
    math = mark('mathematics')
    com = mark('computer')

    sum_five_sub = phys + chem + bio + math + com
    percent = sum_five_sub/500 *100 # total_score/max_score * 100
    
    if percent >= 90:
          grade = 'A'
    elif percent >= 80:
          grade = 'B'
    elif percent >= 70:
          grade = 'C'
    elif percent >= 60:
          grade = 'D'
    elif percent >= 40:
          grade = 'E'
    else:
          grade = 'F'
    
    print(f'Percentage = {percent:.2f}%\nGrade = {grade}')

    user_ans = input('\nDo you want to continue? (y/n): ')

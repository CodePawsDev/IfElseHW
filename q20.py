'''
input basic salary of an employee and calculate its Gross salary according to following:
Basic Salary <= 10000 : HRA = 20%, DA = 80%
Basic Salary <= 20000 : HRA = 25%, DA = 90%
Basic Salary > 20000 : HRA = 30%, DA = 95%

Gross salary is the final salary computed after the additions of DA, HRA and other allowances. 
The formula for DA and HRA is

da = basic_salary * (DA/100)
If DA = 80% then the statement becomes da = basic_salary * (80/100). 
Which can also be written as DA = basic_salary * 0.08. 
Likewise you can also derive a formula for HRA.
'''

user_ans = 'y'

while user_ans.lower() == 'y':
    salary = float(input('Enter salary: '))
    while salary < 1:
        salary = float(input('Please enter valid number of salary: '))

    if salary > 20000:
        hra = salary * 0.2
        da = salary * 0.8
        gross = salary + hra + da
    elif salary > 10000:
        hra = salary * 0.25
        da = salary * 0.9
        gross = salary + hra + da
    else:
        hra = salary * 0.3
        da = salary * 0.95
        gross = salary + hra + da
    print('----------------------')
    print(f'Salary = {salary:,.2f}\nHRA = {hra:,.2f}\nDA = {da:,.2f}\nGross salary = {gross:,.2f}')
    print('----------------------')

    user_ans = input('\nDo you want to continue? (y/n): ')

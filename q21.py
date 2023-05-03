'''
input electricity unit charges 
and calculate total electricity bill according to the given condition:

For first 50 units Rs. 0.50/unit
For next 100 units Rs. 0.75/unit
For next 100 units Rs. 1.20/unit
For unit above 250 Rs. 1.50/unit
An additional surcharge of 20% is added to the bill
'''

user_ans = 'y'

# in case rate change in the future
rate1 = 0.5   # first 50 units
rate2 = 0.75  # next 100 units
rate3 = 1.20  # next 100 units
rate4 = 1.50  # units above 250

while user_ans.lower() == 'y':
    unit = int(input('Enter unit charges: '))
    while unit < 1:
        unit = int(input('Please enter valid number of unit charges: '))
    
    if unit <= 50:
        bill = unit * rate1
    elif unit <= 100:
        bill = (50 * rate1) + ((unit - 50) * rate2)
    elif unit <= 250:
        bill = (50 * rate1) + (100 * rate2) + ((unit - 150) * rate3)
    else:
        bill = (50 * rate1) + (100 * rate2) + (100 * rate3) + ((unit - 250) * rate4)
    
    add_surcharge = bill * 0.2
    total_bill = bill + add_surcharge
    print('----------------')
    print(f'Electricity unit charges = {unit:,}\nBill before additional surcharge = {bill:,.2f}\nAdditional surcharge = {add_surcharge:,.2f}\nTotal = {total_bill:,.2f}')
    print('----------------')

    user_ans = input('\nDo you want to continue? (y/n): ')

# calculate profit or loss.

user_ans = 'y'

while user_ans.lower() == 'y':
    cost = float(input('Enter cost: '))
    while cost < 1:
        cost = float(input('Please enter valid cost: '))

    selling_price = float(input('Enter selling price: '))
    while selling_price < 1:
        selling_price = float('Please enter valid selling price: ')

    if selling_price > cost:
        print(f'profit = {selling_price-cost}')
    elif selling_price < cost:
        print(f'loss = {cost-selling_price}')
    else:
        print('Break-even point.') 

    user_ans = input('\nDo you want to continue? (y/n): ')

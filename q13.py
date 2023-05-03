# count total number of notes in given amount.
# โปรแกรมแลกเงิน [1000,500,100,50,20,10,5,1]

user_ans = 'y'
bank_notes = [1000, 500, 100, 50, 20, 10, 5, 1] # bank_notes types

while user_ans.lower() == 'y':
    total = int(input('Enter amount: '))
    while total < 1:
        total = int(input('Please enter valid number: '))
    
    txt = f'\nNumber of notes\n'
    for each_bank in bank_notes:
        if total//each_bank > 0:
            bank_n = total//each_bank # total for each bank notes
            total %= each_bank # total left
            txt += f'{each_bank}: {bank_n}\n'

    print(txt + 'finished')

    user_ans = input('\nDo you want to continue? (y/n): ')

# input any alphabet and check whether it is vowel or consonant.

user_ans = 'y'
vowel = ['a','e','i','o','u']

while user_ans.lower() == 'y':
    alphabet = input('Enter alphabet: ')
    if alphabet in vowel:
        print(f'{alphabet} is vowel.')
    else:
        print(f'{alphabet} is consonant.')

    user_ans = input('\nDo you want to continue? (y/n): ')
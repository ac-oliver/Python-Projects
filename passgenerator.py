# password generator

import random

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
numbers = '1234567890'
symbols = ',./;!@#$%^&*'

rand_up = ''
rand_low = ''
rand_numbers = ''
rand_symbols = ''

user_upper = int(input('Excellent. Okay. How many upper case letters do you need?'))
user_lower = int(input('How many lower case letters do you need?'))
user_numbers = int(input('And how many numbers?'))
user_symbols = int(input('And, of course, how many symbols?'))

# pass_length = int(input('How many characters does your password need to be?'))

print('Here is your password:')

for u in range(user_upper):
    rand_up += random.choice(upper)
for l in range(user_lower):
    rand_low += random.choice(lower)
for l in range(user_numbers):
    rand_low += random.choice(numbers)
for l in range(user_symbols):
    rand_low += random.choice(symbols)

password = (rand_up + rand_low + rand_numbers + rand_symbols)
random.shuffle(password)
print(password)

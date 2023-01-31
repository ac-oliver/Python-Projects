import random

roll = 'yes' or 'y'

input('Press ENTER to roll the dice.')

while roll == 'yes':
    print(random.randint(1,6))

    input('Roll again?')



import random

roll = 'yes' or 'y'

input('Press ENTER to roll the dice.')

def play(x):
    while roll == 'yes':
        user_roll = random.randint(1,6)
        comp_roll = random.randint(1,6)
        print(f'Your first number is {user_roll}')
        print(f'The computer\'s first number is {comp_roll}')

        if user_roll == comp_roll:
            print(f'Oo, you both rolled a {user_roll}. Doubles!')

        input('Roll again?')
        
        user_roll_two = random.randint(1,6)
        comp_roll_two = random.randint(1,6)
        print(f'Your second number is {user_roll_two}')
        print(f'The computer\'s second number is {comp_roll_two}')

        if user_roll == user_roll_two:
            print(f'Double {user_roll}\'s! You win!')
        elif comp_roll == comp_roll_two:
            print(f'Doubles! But not for you. You lose.')
        elif user_roll == user_roll_two and comp_roll == comp_roll_two:
            print(f'Double doubles! Both win, or both lose?')

        input('Press ENTER to play again.')

play(10)

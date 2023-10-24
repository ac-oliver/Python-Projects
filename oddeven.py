#Small script checking if a number is odd or even

number = input('Enter a number: ')

def odd_even(number):
    if (int(number)%2) == 0:
        print('This is an even number.')
    else:
        print('This is an odd number.')

odd_even(number)
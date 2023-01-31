#Calculator

operations = ['1. Addition',
              '2. Subtraction',
              '3. Multiplication',
              '4. Division']

invalid = 'Invalid Choice.'

for item in operations:
    print(item)
    
while True:
    choice = input('Pick your operation:')
    if(choice == str(1)):
        print('You have chosen addition.')
        first_num = int(input('First Number:'))
        print(' ')
        second_num = int(input('Second Number:'))
        print(' ')
        addition = (first_num + second_num)
        print('The answer is:', addition)
    elif(choice == str(2)):
        print('You have chosen Subtraction.')
        print(' ')
        first_num = int(input('First Number:'))
        print(' ')
        second_num = int(input('Second Number:'))
        print(' ')
        subtraction = (first_num - second_num)
        print('The answer is:', subtraction)
    elif(choice == str(3)):
        print('You have chosen Multiplication.')
        print(' ')
        first_num = int(input('First Number:'))
        print(' ')
        second_num = int(input('Second Number:'))
        print(' ')
        multiplication = (first_num * second_num)
        print('The answer is:', multiplication)
    else:
        print('You have chosen Division.')
        print(' ')
        first_num = int(input('First Number:'))
        print(' ')
        second_num = int(input('Second Number:'))
        print(' ')
        division = (first_num / second_num)
        print('The answer is:', division)


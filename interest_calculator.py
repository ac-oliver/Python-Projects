#Here's a script one can use to determine how much money they'll have after an initial investment and a set interest rate

principal = int(input('Enter initial investment: '))
rate = int(input('Enter an interest rate: '))
time = int(input('What is your time span?'))

def end_invest(principal, rate, time):
    total = principal * (pow((1 + rate / 100), time))
    CI = total - principal
    print('Compound interest earned over ' + str(time) + ' is: ', '${:,.2f}'.format(CI))
    print('Total after ' + str(time) + ' years is: ', '${:,.2f}'.format(total))

end_invest(principal, rate, time)
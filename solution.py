# Task 1
i = 1
big = 999
devil = 666
big_numbers = False

while i <= 3:
    i += 1
    number1 = int(input('Enter first number: '))
    number2 = int(input('Enter second number: '))
    print('\n')
    
    if number1 == devil or number2 == devil:
        print('Whats wrong with you?')
    
    if number1 > number2:
        print('Number 1 is bigger than Number 2')
    elif number1 < number2:
        print('Number 2 is bigger than Number 1')
    elif number1 == number2:
        print('The Numbers are equal')
    else:
        print('The numbers are equal')
    
    if number1 > 999 and number2 > 999:
        print('Number 1 and 2 are big Numbers')
        big_numbers = True
    elif number1 > big:
        print('Number 1 is a big Number')
        big_numbers = True
    elif number2 > big:
        print('Number 2 is a big Number')
        big_numbers = True
    else:
        print('Both Numbers are small')
        big_numbers = False
    
    print('big_numbers is set to: ', big_numbers, '\n')
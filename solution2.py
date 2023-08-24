# Task 2
test = 0

months = {'January': 31,
          'February': 28,
          'March': 31,
          'April': 30,
          'May': 31,
          'June': 30,
          'July': 31,
          'August': 31,
          'September': 30,
          'October': 31,
          'November': 30,
          'December': 31}

print('List of months: ')
for key in months.keys():
    print(key, end=', ')

print('\n')
user_input = input('Input the name of Month: ')
user_input = user_input.capitalize()

for compare in months.keys():
    if compare == user_input:
        print('The month has', months[compare], 'days')
        test = 1
    else:
        continue

if test == 0:
    print('Your Input is not in the List')
        
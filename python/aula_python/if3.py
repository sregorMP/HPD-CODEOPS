age = int(input("enter your age: "))
have_own_car = input('Do you own your own car: ')

if age >= 21:
    if have_own_car == 'y':
      print('You are over 21 years old and own your own car')
    else:
      print('You are over 21 years old and  you do not own your own car')
else:
    if have_own_car == 'y':
      print('You are 21 years and you own your own car')
    else:
      print('You are over 21 years old and you do not own your own car')


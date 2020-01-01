age = int(input("enter your age: "))
have_own_car = input('Do you own your own car: ')

if (age > 21) and (have_own_car == 'y'):
    print('You are over 21 years old and own your own car')

if (age > 21) and (have_own_car == 'n'):
    print('You are over 21 years old and you do not own your own car')

if (age == 21) and (have_own_car == 'y'):
    print('You are 21 years and you own your own car')

if (age == 21) and (have_own_car == 'n'):
    print('You are 21 years old and you do not own your own car')

if (age < 21) and (have_own_car == 'y'):
    print('You are younger 21 years and own your own car')

if (age < 21) and (have_own_car == 'n'):
    print('You are younger 21 years and you do not own your own car')

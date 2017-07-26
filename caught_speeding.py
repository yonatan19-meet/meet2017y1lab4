your_speed = int(input('what is your speed?'))
is_birthday = input('is it your birthday?')

if is_birthday == 'True':
    if your_speed < 36:
        print('no ticket')
    elif your_speed > 35 and your_speed < 56:
        print('small ticket')
    else:
        print('big ticket')

elif is_birthday == 'False':
    if your_speed < 31:
        print('no ticket')
    elif your_speed > 30 and your_speed < 51:
        print('small ticket')
    else:
        print('big ticket')

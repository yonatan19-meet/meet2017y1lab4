strawberries = int(input('What is the number of strawberries'\
                         ' that you bring to the party?'))
What_day = input("Is it a weekday or weekend?")
if What_day == 'weekend' and strawberries > 39:
    print('Fun')

elif What_day == 'weekend' and strawberries <= 39:
    print('Not Fun')

elif What_day == 'weekday' and strawberries < 61 and strawberries > 39:
    print('Fun')

elif What_day == 'weekday' and (strawberries >= 61 or strawberries <= 39):
    print('Not Fun')
else:
    print('Error! Invalid answers!')
    

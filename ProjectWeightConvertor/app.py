import math

weight = float(input('Enter your weight: '))
measureFactor = input('Enter (L)Lbs or (K)Kgs: ')

if (measureFactor.lower() == 'l'):
    weight = weight * 0.45359
    print(f'Your weight in Kgs is : {round(weight,2)}')
else:
    weight = weight / 0.45359
    print(f'Your weight in Lbs is : {round(weight,2)}')
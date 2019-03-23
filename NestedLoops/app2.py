numbers = [0,1,2,3,4,5,4,3,2,1,1,1,4,6,7,8,9,9,9,9,8,7,7,6,5,5,5,6,7,8,8,7,6,5,5,4,4,3,3,3,3,3,3,2,2,3,3]
x = 'x'

for number in numbers:
    output = ''
    for count in range(number):
        output += '0'
    print(f'''     {output}''')
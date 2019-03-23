#fisrt used portional argument and then use key word argument or elsepython throws error

def great_user(first_name,last_name,age):
    print(f'Hi {first_name} {last_name} {age}')
    print('Welcome Aboard')


print("Start")
great_user(last_name="Smith",first_name="John",age=40)
great_user("John","Smith",age=30)
#great_user(last_name="Smith","John") this is eg of the note
print("Finish")
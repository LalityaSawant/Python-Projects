class Person:
    def __init__(self,name):
        self.name = name


    def talk(self,message):
        print(message)


    def talk_with_name(self,message):
        print(f'{message} {self.name}')


bob = Person("Bob Smith")
bob.talk(f"Hi, I am {bob.name}")

john = Person("John Smith")
john.talk_with_name("Hi, I am")
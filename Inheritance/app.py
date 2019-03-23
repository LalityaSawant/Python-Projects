class Mamal:
    def walk(self):
        print("walk")

class Dog(Mamal):
    pass
    # if we dont have to have any other code in class so use pass keyword


class Cat(Mamal):
    def meaw(self):
        print("meaw")

dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.meaw()
cat1.walk()
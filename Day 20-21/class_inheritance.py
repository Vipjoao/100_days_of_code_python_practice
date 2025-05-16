
class Animal:
    def __init__(self):
        self.name = "Name"
        self.age = "Age"

    def breathe(self):
        print("Inhale, exhale")

    def eat(self):
        print("the animal is eating")


class Fish(Animal): # Fish will inherit Animal as its super
    def __init__(self):
        super().__init__() # Fish inherits its class '__init__' from his super "Animal"

    def breathe(self):
        super().breathe() # We can create a method breathe for the fish by having the "Animal" method for a basis
        print("doing this underwater")

nemo = Fish()
nemo.eat() # As fish inherited "Animal", he can use the functions from its superclass, such as 'eat'
nemo.breathe()
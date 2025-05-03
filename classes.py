#Python classes are blueprints for creating objects
#it defines what attributes (data) and actions (methods) the objective will have. 

class Dog:

    species="Canis lupus familiaris"

    def __init__(self, name, breed, age):
        self.name=name #these are attributes of the class
        self.breed=breed
        self.age=age

    def bark_dog1(self): #these are methods
        print(f"{self.name} says woof!")

    def bark_dog2(self):
        print(f"{self.name} says yelp!")

    def bark_dog3(self):
        print(f"{self.name} says woooo!")

    def desctiption(self):
        print(f"{self.name} is a {self.age}-year old {self.breed} and is part of the {Dog.species}")

class GuardDog(Dog):
    def bark(self):
        print(f"{self.name} says Grrr!")

#class Dog defines a new class called Dog
#_init_ This is the constructor, it runs when you create the dog object. 

my_Dog1=Dog("Zurie", "catahoula",4)
my_Dog1.bark_dog1()
my_Dog1.desctiption()

my_Dog2=Dog("Renegade", "Austrlian Shephard",5)
my_Dog2.bark_dog2()
my_Dog2.desctiption()

my_Dog3=Dog("Kai", "Husky",5)
my_Dog3.bark_dog3()
my_Dog3.desctiption()



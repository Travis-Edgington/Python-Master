#Python classes are blueprints for creating objects
#it defines what attributes (data) and actions (methods) the objective will have. 

# class Dog:

#     species="Canis lupus familiaris"

#     def __init__(self, name, breed, age):
#         self.name=name #these are attributes of the class
#         self.breed=breed
#         self.age=age

#     def bark_dog1(self): #these are methods
#         print(f"{self.name} says woof!")

#     def bark_dog2(self):
#         print(f"{self.name} says yelp!")

#     def bark_dog3(self):
#         print(f"{self.name} says woooo!")

#     def desctiption(self):
#         print(f"{self.name} is a {self.age}-year old {self.breed} and is part of the {Dog.species}")

# class GuardDog(Dog):
#     def bark(self):
#         print(f"{self.name} says Grrr!")

# #class Dog defines a new class called Dog
# #_init_ This is the constructor, it runs when you create the dog object. 

# my_Dog1=Dog("Zurie", "catahoula",4)
# my_Dog1.bark_dog1()
# my_Dog1.desctiption()

# my_Dog2=Dog("Renegade", "Austrlian Shephard",5)
# my_Dog2.bark_dog2()
# my_Dog2.desctiption()

# my_Dog3=Dog("Kai", "Husky",5)
# my_Dog3.bark_dog3()
# my_Dog3.desctiption()


# class Policy:
#     def __init__(self, number, premium):
#         self.number=number
#         self.premium=premium
    
#     @classmethod
#     def from_string(cls, policy_string):
#         number, premium=policy_string.split(",")
#         return cls(number, float(premium))
# policy=Policy.from_string("ABCD123,1200")
# print(policy.number, policy.premium)

# import datetime

# class Policy:
#     def __init__(self, policy_number, written_premium, effective_date, expiration_date):
#         self.policy_number=policy_number
#         self.written_premium=written_premium
#         self.effective_date=effective_date
#         self.expiration_date=expiration_date
#         self.claims=[]

#     def add_claim(self, claim_amount):
#         self.claims.append(claim_amount)
#     def total_claims(self):
#         return sum(self.claims)
#     def earned_premium(self, calendar_start, calendar_end):
#         start=max(self.effective_date, calendar_start)
#         end=max(self.expiration_date, calendar_end)
#         overlap_days=max((end-start).days,0)
#         policy_days=(self.expiration_date-self.effective_date).days

#         if policy_days==0:
#             return 0
#         return self.written_premium*(overlap_days/policy_days)
    
#     def loss_ratio(self, calendar_start, calendar_end):
#         earned=self.earned_premium(calendar_start, calendar_end)
#         if earned ==0:
#             return 0
#         return self.total_claims()/earned

 
# calendar_start=datetime.date(2020,1,1)
# calendar_end=datetime.date(2021,6,1)   
# test_Polciy=Policy("ABCD124", 1000, datetime.date(2021,1,1), datetime.date(2021,7,1))
# print(test_Polciy.earned_premium(calendar_start, calendar_end))


# class Example:
#     def say_hello(self):
#         print("hello from the object")

# obj=Example()

# obj.say_hello()

# class Example:
#     @classmethod
#     def say_hello(self):
#         print("hello from the object")

# Example.say_hello()

# def old_classmethod(func):
#     return classmethod(func)

# def method(cls):
#     pass
# method=old_classmethod(method)

#Method 1
# def my_decorator(func):
#     def wrapper():
#         print("before the function runs")
#         func()
#         print("after the functions runs")

#     return wrapper

# def say_hello():
#     print("Hello")

# say_hello=my_decorator(say_hello)
# say_hello()

# method 2

# def my_decorator(func):
#     def wrapper():
#         print("before the function runs")
#         func()
#         print("after the functions runs")

#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello")


# say_hello()
# def multiply_by_two(func):

#     def wrapper():
#         result=func()
#         return 2*result
#     return wrapper

# #@multiply_by_two
# def Two():
#     return 2


# Two=multiply_by_two(Two)
# print (Two())


#Why do we use classes

#lets do things without classes

# #Policy 1
# policy1_number="A123"
# policy1_premium=1000
# policy1_claims=[200,300]

# #Policy number 2
# policy2_number="B456"
# policy2_premium=1200
# policy2_claims=[500]

# def total_claims(claims):
#     return sum(claims)

# #without classes
# print(total_claims(policy1_claims))

class Policy:
    def __init__(self, number, premium):
        self.number=number
        self.premium=premium
        self.claim=[] #create and attribute of the class that is not input

    def add_claim(self,amount):
        self.claim.append(amount)
    
    def total_claims(self):
        return sum(self.claim)
    
    def loss_ratio(self):
        if self.premium==0:
            return 0
        return self.total_claims()/self.premium

# policy1=Policy("A123",1000)
# policy2=Policy("B456",1200)

# policy1.add_claim(900)
# policy2.add_claim(300)

# policy1.loss_ratio()
# print(f"The loss ration for policy1 is {policy1.loss_ratio()}")

# print(f"The total claims for policy 1 is {policy1.total_claims()}")
# print(f"The total claims for policy 2 is {policy2.total_claims()}")
type(Policy)

print(Policy.__dict__)
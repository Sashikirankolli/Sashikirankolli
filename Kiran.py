
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        return f"{self.name} is {self.age} years old."

class Dog(Pet):
    def bark(self):
        return f"{self.name} says woof!"

class Cat(Pet):
    def meow(self):
        return f"{self.name} says meow!"

# Create instances of Dog and Cat
my_dog = Dog("Fido", 3)
my_cat = Cat("Whiskers", 2)

# Call the show_info method
print(my_dog.show_info())
print(my_cat.show_info())

# Call the bark and meow methods
print(my_dog.bark())
print(my_cat.meow())

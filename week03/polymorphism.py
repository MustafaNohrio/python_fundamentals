class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

class Cow:
    def speak(self):
        print("Moo")

dog = Dog()
cat = Cat()
cow = Cow()

dog.speak()
cat.speak()
cow.speak()

#with inheritance
class Animal:

    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):

    def speak(self):
        print("Bark")

class Cat(Animal):

    def speak(self):
        print("Meow")

dog = Dog()
cat = Cat()

dog.speak()
cat.speak()
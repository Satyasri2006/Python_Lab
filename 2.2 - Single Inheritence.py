class Animal :
    def sound(self) :
        print("Animal makes a sound")
class Dog(Animal) :
    def sound(self) :
        print("Dog barks")
class Cat(Animal) :
    def sound(self) :
        print("Cat meows")
class Lion(Animal) :
    def sound(self) :
        print("Lion roars")
dog=Dog()
cat=Cat()
lion=Lion()
dog.sound()
cat.sound()
lion.sound()

class Animal :
    def make_sound(self) :
        print("Animal makes a sound.")
class Dog (Animal) :
    def make_sound(self) :
        print("Dog barks.")
class Cat (Animal) :
    def make_sound(self) :
        print("Cat meows.")
class Bird (Animal) :
    def make_sound(self) :
        print("Bird chirps.")
a = Animal()
d = Dog()
c = Cat()
b = Bird()

a.make_sound()
d.make_sound()
c.make_sound()
b.make_sound()

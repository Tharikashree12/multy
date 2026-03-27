class animal:
    def eat(self):
        print("animal is eating")
class dog(animal):
    def bark(self):
        print("dog is barking")
class cat(animal):
    def meow(self):
        print("cat is meowing")
d = dog()
c = cat()
d.eat()
d.bark()
c.eat()
c.meow()


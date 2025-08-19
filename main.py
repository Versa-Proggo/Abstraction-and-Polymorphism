from abc import ABC
class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk")
class Snake(Animal):
    def move(self):
        print("I can crawl")
class Dogg(Animal):
    def move(self):
        print("I can bark")
class Lion(Animal):
     def move(self):
        print("I can roar")
h = Human()
h.move()
s = Snake()
s.move()
d = Dogg()
d.move()
l = Lion()
l.move()
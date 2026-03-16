class Animal:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class Cat(Animal):
    def __init__(self, name, age, height, weight, speed):
        super().__init__(self, name, age, height, weight)
        self.speed = speed

class Parrot(Animal):
    def __init__(self, name, age, height, weight, fly):
        super().__init__(self, name, age, age, height, weight,)
        self.fly = fly

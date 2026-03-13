class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def sleep(self):
        print(self.name, "is sleeping")

    def wake_up(self):
        print(self.name, "wakes up")

    def eat(self):
        print(self.name, "is eating")

    def play(self):
        print(self.name, "wants to play")

jambo = Cat("Jambo", 4, "Orange")
jambo.sleep()
jambo.wake_up()
jambo.eat()
jambo.play()
jambo.sleep()
jambo.wake_up()
jambo.eat()
jambo.play()
jambo.sleep()

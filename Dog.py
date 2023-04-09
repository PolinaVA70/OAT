"""
Создать класс Dog:
mood = 50 # 100 - счастливое, 0 - ужасное
hunger = 50 # 100 - сытый, 0 - голод
vivacity = 50 # бодрость 100 - бодрый, 0 - уставший

реализовать методы:
    поспать
        (голод уменьшается на 50% от текущего значения,
        бодрость увеличивается на 50% от текущего значения)
    поиграть
        (настроение увеличивается на 100% от текущего значения,
        бодрость уменьшает на 50% от текущего значения,
        голод уменьшает на 50% от текущего значения)
    поесть
        (голод увеличивается на 100% от текущего значения,
        настроение увеличивается на 25% от текущего значения )
"""

class Dog:

    def __init__(self):
        self.mood = 50
        self.hunger = 50
        self.vivacity = 50  # бодрость

    def sleep(self):
        self.hunger = 25
        self.vivacity = self.vivacity * 1.5

    def play(self):
        self.vivacity = self.vivacity * 0.5
        self.hunger = self.hunger * 0.5
        self.mood = 100

    def eat(self):
        self.vivacity = 100
        self.hunger = 100

dog1 = Dog()
print('dog1\n', 'mood', dog1.mood, 'hunger', dog1.hunger, 'vivacity', dog1.vivacity)
dog1.sleep()
print('dog1\n', 'mood', dog1.mood, 'hunger', dog1.hunger, 'vivacity', dog1.vivacity)
dog1.play()
print('dog1\n', 'mood', dog1.mood, 'hunger', dog1.hunger, 'vivacity', dog1.vivacity)
dog1.eat()
print('dog1\n', 'mood', dog1.mood, 'hunger', dog1.hunger, 'vivacity', dog1.vivacity)
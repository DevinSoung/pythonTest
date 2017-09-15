class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog=Dog()
dog.run();

print(isinstance(dog,Animal))

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

run_twice(Tortoise())

class Timer(object):
    def run(self):
        print('Start...')

run_twice(Timer())
import random

def randomInteger():
    number = random.randint(1,100)
    print(f'Example of Random Integer {number}')

def randomFloatingPoint():
    number = random.random()
    print(f'Example of Random Floating Point {number}')

def randomFloatingRange():
    number = random.uniform(1.5, 10.5)
    print(f'Example of Random Floating Range {number}')

def randomChoice():
    items = ['apple', 'banana', 'cherry', 'date']
    number = random.choice(items)
    print(f'Example of Random Choice {number}')

def randomSample():
    items = ['apple', 'banana', 'cherry', 'date']
    number = random.sample(items, 2)
    print(f'Example of Random Sample {number}')

def randomRange():
    number = random.randrange(0, 10, 2)
    print(f'Example of Random Range {number}')

randomInteger()
randomFloatingPoint()
randomFloatingRange()
randomChoice()
randomSample()
randomRange()
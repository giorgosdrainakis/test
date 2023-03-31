# this is a fruit
import math

class Animal():
    def __init__(self,name):
        self.name=name
        self.size=None

dog=Animal(name='dog')
dog.size=1.5

cat=Animal(name='cat')
cat.size=0.5

print('Cat size='+str(cat.size))
print('Dog size='+str(dog.size))
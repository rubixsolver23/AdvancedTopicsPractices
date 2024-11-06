
from csv import reader

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"Meet {self.name}, a {self.breed}."
    
dogs = []

with open('Dog class/DogsList.csv') as csv_file:
    csv_reader = reader(csv_file, delimiter=',')
    next(csv_reader)
    for name, breed in csv_reader:
        dogs.append(Dog(name, breed))

for dog in dogs:
    print(dog)
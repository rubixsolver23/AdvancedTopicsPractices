# Composition is a type of class that exists inside of another class (class has an other class, inheritince class is the other class)


class Car:
    def __init__(self, make, model, year, engine):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine

    def __str__(self):
        return f"This is a {self.year} {self.make} {self.model}"


class Engine:
    def __init__(self, configuration, displacement, horsepower, torque):
        self.configuration = configuration
        self.displacement = displacement
        self.horsepower = horsepower
        self.torque = torque

    def ignite(self):
        print("Vroom, vroom!")

# To call a composite class you must access where it is saved within the class
myEngine = Engine("V8", 5.8, 326, 344)
myCar = Car("Honda", "Clarity", 2016, myEngine)

print(myCar)
myCar.engine.ignite()



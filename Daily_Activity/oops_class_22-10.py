class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    # Constructor (initializer)
    def init(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age
    
    # Instance method
    def bark(self):
        return f"{self.name} says woof!"
    
    # Another instance method
    def get_age(self):
        return f"{self.name} is {self.age} years old."
class Person:
    species = "humans"

    def __init__(self, name, age):
        
        self.name = name
        self.age = age

   
    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."


person1 = Person("Ishita", 19)
print(person1.introduce())


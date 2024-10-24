class Person:
    species = "humans"

    def __init__(human, name, age):
        
        human.name = name
        human.age = age

   
    def introduce(human):
        return f"My name is {human.name} and I am {human.age} years old."


person1 = Person("Ishita", 19)
print(person1.introduce())


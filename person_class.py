

class Person:
    def __init__(self, name, age) -> None:
        # Atributos:
        self.name = name
        self.age = age

    # Metodos:
    def say_hello(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old')

    
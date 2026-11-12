class Father:
    def __init__(self, name="Tarzan"):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name}, your father."


class Mother:
    def __init__(self, name="Jane"):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name}, your mother."

class Child(Father, Mother):
    def __init__(self, name, father_name, mother_name):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)
        self.name = name

    def greet(self):
        father_greeting = Father.greet(self)
        mother_greeting = Mother.greet(self)
        return f"{father_greeting} {mother_greeting} I am {self.name}, your child."

# Example usage
child = Child("Charlie", "John", "Jane")
print(child.greet())

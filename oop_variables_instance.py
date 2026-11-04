
# Public instance variables are accessible from outside the class, while private instance variables are not.
# In Python, we can make an instance variable private by prefixing it with double underscores.
# This is known as name mangling, and it changes the name of the variable in a way that makes it
# harder to access from outside the class.

# Using instance variables without double underscores (public instance variables).

class ExampleClass:
    def __init__(self, val = 1):
        self.first = val

    def set_second(self, val):
        self.second = val


example_object_1 = ExampleClass()
example_object_1.set_second(2)

example_object_2 = ExampleClass(2)
example_object_2.set_second(3) # This will create a public instance variable 'second' for 'example_object_2' with the value 3.

example_object_3 = ExampleClass(4)
example_object_3.third = 5 # This will create a public instance variable 'third' for 'example_object_3'.
example_object_3.second = 7 # This will create a public instance variable 'second' for 'example_object_3'.
example_object_3.set_second(8) # This will overwrite the public instance variable 'second' for 'example_object_3' with the value 8.


print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)


# =======================


# Using double underscores to make instance variables private.
class ExampleClass2:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val = 2):
        self.__second = val


example_object_1 = ExampleClass2()
example_object_2 = ExampleClass2(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass2(4)
example_object_3.__third = 5 # This will not create a private instance variable, but rather a public one with the name '__third'.


print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

# The output of the above code will be:
# {'_ExampleClass2__first': 1}
# {'_ExampleClass2__first': 2, '_ExampleClass2__second': 3}
# {'_ExampleClass2__first': 4, '__third': 5}


print(example_object_1._ExampleClass2__first) # This will print the value of the private instance variable '__first' of 'example_object_1', which is 1.
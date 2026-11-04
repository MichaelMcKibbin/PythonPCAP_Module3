# Python provides a function hasattr which is able to safely check if any object/class contains a specified property.
# It expects two arguments to be passed to it:
# the class or the object being checked;
# the name of the property whose existence has to be reported (note: must be a string containing the attribute name)
# The function returns True or False.


class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)
print(example_object.a)

# if hasattr(example_object, 'b'):
#     print(example_object.b)

try:
    print(example_object.b)
except AttributeError:
    pass

#=====================

class ExampleClass2:
    a = 1
    def __init__(self):
        self.b = 2


example_object2 = ExampleClass2()

print(hasattr(example_object2, 'b'))
print(hasattr(example_object2, 'a'))
print(hasattr(ExampleClass2, 'b'))
print(hasattr(ExampleClass2, 'a'))

#=====================

class ExampleClass3:
    attr = 1


print(hasattr(ExampleClass3, 'attr'))
print(hasattr(ExampleClass3, 'prop'))


#=====================

class Sample:
    gamma = 0 # Class variable.
    def __init__(self):
        self.alpha = 1 # Instance variable.
        self.__delta = 3 # Private instance variable.


obj = Sample()
obj.beta = 2  # Another instance variable (existing only inside the "obj" instance.)
print(obj.__dict__)
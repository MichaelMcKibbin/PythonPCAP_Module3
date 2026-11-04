class MyClass:
    pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5


def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)


print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)


# Reflection and introspection enable a programmer to do anything with any object, no matter where it comes from.
#
# The function named incIntsI() gets an object of any class, scans its contents in order to
# find all integer attributes with names starting with i, and increments them by one.
#
# How it works:
#
# line 1: define a simple class...
# lines 5 through 11: ... and fill it with some attributes;
# line 14: this is the function
# line 15: scan the __dict__ attribute, looking for all attribute names;
# line 16: if a name starts with i...
# line 17: ... use the getattr() function to get its current value;
#  note: getattr() takes two arguments: an object, and its property name (as a string), and returns the current attribute's value;
# line 18: check if the value is of type integer, and use the function isinstance()
#  To do that; isinstance() takes two arguments: an object, and a type, and returns True if the object is of that type, or False otherwise;
# line 19: if the check goes well, increment the property's value by making use of the setattr() function;
#  The function takes three arguments: an object, the property name (as a string), and the property's new value.
#
# The code outputs:
#
# {'a': 1, 'integer': 4, 'b': 2, 'i': 3, 'z': 5, 'ireal': 3.5}
# {'a': 1, 'integer': 5, 'b': 2, 'i': 4, 'z': 5, 'ireal': 3.5}

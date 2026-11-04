# The __name__ attribute of a class is a string that contains the name of the class.
# It can be accessed using the class name or an instance of the class.

class Classy:
    pass # This is a simple class with no attributes or methods

print(Classy.__module__)
obj = Classy()
print(obj.__module__)

# Output:
# __main__
# __main__

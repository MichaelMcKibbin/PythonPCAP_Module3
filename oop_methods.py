# The self parameter is a reference to the current instance of the class,
# and is used to access variables that belong to the class.
# The self parameter is also used to invoke other object/class methods from inside the class.

class Classy:
    varia = 2
    def method(self):
        print(self.varia, self.var)


obj = Classy()
obj.var = 3
obj.method()

# Output:
# 2 3

#=====================

class Classy2:
    def other(self):
        print("other")

    def method(self):
        print("method")
        self.other()


obj = Classy2()
obj.method()

# Output:
# method
# other

#=====================

# If you name a method like this: __init__, it won't be a regular method - it will be a constructor.
#
# If a class has a constructor, it is invoked automatically and implicitly when the object of the class is instantiated.
#
# The constructor:
#
# 1. is obliged to have the self parameter (it's set automatically, as usual);
# 2. may (but doesn't need to) have more parameters than just self;
#    if this happens, the way in which the class name is used to create the object must reflect the __init__ definition;
# 3. can be used to set up the object,
#    i.e., properly initialize its internal state,
#    create instance variables,
#    instantiate any other objects if their existence is needed, etc.

class Classy3:
    def __init__(self, value):
        self.var = value


obj_1 = Classy3("object")

print(obj_1.var)

# Output:
# object

# The constructor:
#  Cannot return a value, as it is designed to return a newly created object and nothing else;
#  Cannot be invoked directly either from the object or from inside the class
#  (you can invoke a constructor from any of the object's subclasses)

#=====================

# Property name mangling is a technique used in Python to make class attributes (variables and methods) private
# by changing their names in a way that makes them harder to access from outside the class.
# This is done by prefixing the attribute name with double underscores (__).

class Classy4:
    def visible(self):
        print("visible")

    def __hidden(self):
        print("hidden")


obj = Classy4()
obj.visible()

try:
    obj.__hidden()
except:
    print("failed")

obj._Classy4__hidden()

# Output:
# visible
# failed
# hidden

#=====================

class Classy5:
    def __init__(self, value = None):
        self.var = value


obj_1 = Classy5("object")
obj_2 = Classy5()

print(obj_1.var)
print(obj_2.var)

# Output:
# object
# None

#=====================


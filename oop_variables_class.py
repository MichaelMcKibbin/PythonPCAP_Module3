# Class variables are shared across all instances of the class, while instance variables are unique to each instance.
# In this example, the class variable `counter` keeps track of how many instances of `ExampleClass` have been created.
# Each time a new instance is created, the `counter` is incremented by 1.
# The instance variable `__first` is unique to each instance and is initialized with the value passed to the constructor.
#
# A class variable always presents the same value in all class instances (objects)

# class ExampleClass:
#     counter = 0
#     def __init__(self, val = 1):
#         self.__first = val
#         ExampleClass.counter += 1
#
#
# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
# example_object_3 = ExampleClass(4)
#
# print(example_object_1.__dict__, example_object_1.counter)
# print(example_object_2.__dict__, example_object_2.counter)
# print(example_object_3.__dict__, example_object_3.counter)


# ======================

# Mangling a class variable's name using double underscores

# class ExampleClass2:
#     __counter = 0
#     def __init__(self, val = 1):
#         self.__first = val
#         ExampleClass2.__counter += 1
#
#
# example_object_1 = ExampleClass2()
# example_object_2 = ExampleClass2(2)
# example_object_3 = ExampleClass2(4)
#
# print(example_object_1.__dict__, example_object_1._ExampleClass2__counter)
# print(example_object_2.__dict__, example_object_2._ExampleClass2__counter)
# print(example_object_3.__dict__, example_object_3._ExampleClass2__counter)


# ======================

class ExampleClass3:
    varia = 1
    def __init__(self, val):
#        self.varia = val
        ExampleClass3.varia = val
#        varia=val



print(ExampleClass3.__dict__)
print("x")

example_object = ExampleClass3(2)

print(ExampleClass3.__dict__)
print("xx")
print(example_object.__dict__)
print("xxx")
print(example_object.varia)
print("xxxx")
print(ExampleClass3.varia)

# Note 1: When using ExampleClass3.varia = val, we are modifying the class variable varia, which is shared across all instances of the class.
# This means that if we create multiple instances of ExampleClass3, they will all share the same value of varia.
# print(ExampleClass3.__dict__) output is: {'__module__': '__main__', '__firstlineno__': 46, 'varia': 1, '__init__': <function ExampleClass3.__init__ at 0x000001F1E9E63060>, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'ExampleClass3' objects>, '__weakref__': <attribute '__weakref__' of 'ExampleClass3' objects>, '__doc__': None}

# Note 2: When using self.varia = val, we are creating an instance variable varia that is unique to each instance of the class.
#  This means that if we create multiple instances of ExampleClass3, each instance will have its own value of varia, and modifying the value of varia in one instance will not affect the value of varia in other instances.
# print(example_object.__dict__) output is: {'__module__': '__main__', '__firstlineno__': 46, 'varia': 2, '__init__': <function ExampleClass3.__init__ at 0x000001F1E9E63060>, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'ExampleClass3' objects>, '__weakref__': <attribute '__weakref__' of 'ExampleClass3' objects>, '__doc__': None}

# Note 3: When using varia = val, we are creating a local variable varia that is only accessible within the __init__ method.
# This means that if we create multiple instances of ExampleClass3, each instance will not have its own value of varia, and modifying the value of varia in one instance will not affect the value of varia in other instances.

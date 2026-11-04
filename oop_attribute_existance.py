# # Not all instances of a class have the same attributes.
# # This can be confusing when trying to access an attribute that may not exist for a particular instance.
#
# class ExampleClass:
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1
#
#
# example_object = ExampleClass(1)
#
# print(example_object.a)
# print(example_object.b)
#
# # Output:
# # 1
# # Traceback (most recent call last):
# #   File ".main.py", line 11, in
# #     print(example_object.b)
# # AttributeError: 'ExampleClass' object has no attribute 'b'

#=====================

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)
print(example_object.a)

try:
    print(example_object.b)
except AttributeError:
    pass

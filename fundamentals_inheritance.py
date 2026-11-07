

# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy
#
# sun = Star("Sun", "Milky Way")
#
# print(sun) # This will print the memory address of the sun object, not its attributes.
# print(sun.name)
# print(sun.galaxy)
#

class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

# defining the __str__ method to provide a string representation of the object
    def __str__(self):
        return self.name + ' in ' + self.galaxy

sun = Star("Sun", "Milky Way")

print(sun) # This will now print "Sun in Milky Way" because of the __str__ method.
print()
print()

#=========================
print("==========================")
print()

class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass

# Checking subclass relationships

for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end="\t")
    print()

print()
print()

# Instance checking

my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()

#=========================
print("==========================")
print()

# The is operator checks if two references point to the same object in memory,
# while the == operator checks if the values of the objects are equal.
#
# The is operator checks whether two variables (object_one and object_two here) refer to the same object.
# Variables don't store the objects themselves, but only the handles pointing to the internal Python memory.
#
# Assigning a value of an object variable to another variable doesn't copy the object, but only its handle (memory location reference).
#

class SampleClass:
    def __init__(self, val):
        self.val = val


object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1

print(object_1 is object_2)
print(object_2 is object_3)
print(object_3 is object_1)
print(object_1.val, object_2.val, object_3.val)

string_1 = "Mary had a little "
string_2 = "Mary had a little lamb"
string_1 += "lamb"

print(string_1 == string_2, string_1 is string_2)

#=========================
print("==========================")
print()

# inheriting methods

class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)


obj = Sub("Andy")

print(obj)

#=========================
print("==========================")
print()

# the super() function is used to call a method from the parent class.
# It is often used in the __init__ method of a subclass to ensure that the parent class is properly initialized.

class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        super().__init__(name)


obj = Sub("Andy")

print(obj)

#=========================
print("==========================")

# Testing properties: class variables.
class Super:
    supVar = 1


class Sub(Super):
    subVar = 2


obj = Sub()

print(obj.subVar)
print(obj.supVar)

#==========================
print("==========================")

# Testing properties: instance variables.
class Super:
    def __init__(self):
        self.supVar = 11


class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12


obj = Sub()

print(obj.subVar)
print(obj.supVar)

#==========================
print("==========================")

# When you try to access any object's entity, Python will try to (in this order):
#
#
# find it inside the object itself;
# find it in all classes involved in the object's inheritance line from bottom to top;

# three-level inheritance

class Level1:
    variable_1 = 100

    def __init__(self):
        self.var_1 = 101

    def fun_1(self):
        return 102


class Level2(Level1):
    variable_2 = 200

    def __init__(self):
        super().__init__()
        self.var_2 = 201

    def fun_2(self):
        return 202


class Level3(Level2):
    variable_3 = 300

    def __init__(self):
        super().__init__()
        self.var_3 = 301

    def fun_3(self):
        return 302


obj = Level3()

print(obj.variable_1, obj.var_1, obj.fun_1())
print(obj.variable_2, obj.var_2, obj.fun_2())
print(obj.variable_3, obj.var_3, obj.fun_3())

#==========================
print("==========================")
print()
#Multiple inheritance occurs when a class has more than one superclass.
# Syntactically, such inheritance is presented as a comma-separated list of superclasses put inside parentheses after the new class name
#
# The Sub class has two superclasses: SuperA and SuperB.
# This means that the Sub class inherits all the goods offered by both SuperA and SuperB.

class SuperA:
    var_a = 10
    def fun_a(self):
        return 11


class SuperB:
    var_b = 20
    def fun_b(self):
        return 21


class Sub(SuperA, SuperB):
    pass


obj = Sub()

print(obj.var_a, obj.fun_a())
print(obj.var_b, obj.fun_b())

#==========================
print("==========================")
print()

# Overriding methods and properties
# Python looks for an entity from bottom to top, and is fully satisfied with the first entity of the desired name.

class Level1:
    var = 100
    def fun(self):
        return 101


class Level2(Level1):
    var = 200
    def fun(self):
        return 201


class Level3(Level2):
    pass


obj = Level3()

print(obj.var, obj.fun())

#==========================
print("==========================")
print()

# Python looks for object components in the following order:
#
# inside the object itself;
# in its superclasses, from bottom to top;
# if there is more than one class on a particular inheritance path, Python scans them from left to right.

class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"


class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"


class Sub(Left, Right):
    pass


obj = Sub()

print(obj.var, obj.var_left, obj.var_right, obj.fun())


class Sub2(Right, Left):
    pass


obj2 = Sub2()

print(obj2.var, obj2.var_left, obj2.var_right, obj2.fun())

#===========================
print("==========================")
print()

# polymorphism

class One:
    def do_it(self):
        print("do_it from One")

    def doanything(self):
        self.do_it()


class Two(One):
    def do_it(self):
        print("do_it from Two")


one = One()
two = Two()

one.doanything()
two.doanything()

#===========================
print("==========================")
print()

# hierarchy of classes using composition

import time

class Tracks:
    def change_direction(self, left, on):
        print("tracks: ", left, on)


class Wheels:
    def change_direction(self, left, on):
        print("wheels: ", left, on)


class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)


wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())

wheeled.turn(True)
tracked.turn(False)

#============================
print("==========================")
print()

# Key takeaways
#
# 1. A method named __str__() is responsible for converting an object's contents into a (more or less) readable string. You can redefine it if you want your object to be able to present itself in a more elegant form. For example:
#
# class Mouse:
#     def __init__(self, name):
#         self.my_name = name
#
#
#     def __str__(self):
#         return self.my_name
#
#
# the_mouse = Mouse('mickey')
# print(the_mouse)  # Prints "mickey".
#
#
# 2. A function named issubclass(Class_1, Class_2) is able to determine if Class_1 is a subclass of Class_2. For example:
#
# class Mouse:
#     pass
#
#
# class LabMouse(Mouse):
#     pass
#
#
# print(issubclass(Mouse, LabMouse), issubclass(LabMouse, Mouse))  # Prints "False True"
#
#
# 3. A function named isinstance(Object, Class) checks if an object comes from an indicated class. For example:
#
# class Mouse:
#     pass
#
#
# class LabMouse(Mouse):
#     pass
#
#
# mickey = Mouse()
# print(isinstance(mickey, Mouse), isinstance(mickey, LabMouse))  # Prints "True False".
#
#
# 4. A operator called is checks if two variables refer to the same object. For example:
#
# class Mouse:
#     pass
#
#
# mickey = Mouse()
# minnie = Mouse()
# cloned_mickey = mickey
# print(mickey is minnie, mickey is cloned_mickey)  # Prints "False True".
#
#
#
# 5. A parameterless function named super() returns a reference to the nearest superclass of the class. For example:
#
# class Mouse:
#     def __str__(self):
#         return "Mouse"
#
#
# class LabMouse(Mouse):
#     def __str__(self):
#         return "Laboratory " + super().__str__()
#
#
# doctor_mouse = LabMouse();
# print(doctor_mouse)  # Prints "Laboratory Mouse".
#
#
# 6. Methods as well as instance and class variables defined in a superclass are automatically inherited by their subclasses. For example:
#
# class Mouse:
#     Population = 0
#     def __init__(self, name):
#         Mouse.Population += 1
#         self.name = name
#
#     def __str__(self):
#         return "Hi, my name is " + self.name
#
# class LabMouse(Mouse):
#     pass
#
# professor_mouse = LabMouse("Professor Mouser")
# print(professor_mouse, Mouse.Population)  # Prints "Hi, my name is Professor Mouser 1"
#
#
# 7. In order to find any object/class property, Python looks for it inside:
#
# the object itself;
# all classes involved in the object's inheritance line from bottom to top;
# if there is more than one class on a particular inheritance path, Python scans them from left to right;
# if both of the above fail, the AttributeError exception is raised.
#
# 8. If any of the subclasses defines a method/class variable/instance variable of the same name as existing in the superclass, the new name overrides any of the previous instances of the name. For example:
#
# class Mouse:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return "My name is " + self.name
#
# class AncientMouse(Mouse):
#     def __str__(self):
#         return "Meum nomen est " + self.name
#
# mus = AncientMouse("Caesar")  # Prints "Meum nomen est Caesar"
# print(mus)
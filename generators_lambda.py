two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))

#==========================
print("==========================")
print()

def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')


def poly(x):
    return 2 * x**2 - 4 * x + 2
    # f(x) = 2(x^2) - 4x + 2


print_function([x for x in range(-2, 3)], poly)

#==========================
print("==========================")
print()

# without defining a function (poly), we can use a lambda expression to define the function in place

def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')

print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

#==========================
print("==========================")
print()

# Lambdas and the map() function

list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()

# build the list_1 with values from 0 to 4;
# next, use map along with the first lambda to create a new list in which all elements have been
# evaluated as 2 raised to the power taken from the corresponding element from list_1;
# list_2 is printed then;
# in the next step, use the map() function again to make use of the generator it returns
# and to directly print all the values it delivers; as you can see, we've engaged the second lambda here
# - it just squares each element from list_2.


#==========================
print("==========================")
print()

# Lambdas and the filter() function

from random import seed, randint

seed()
data = [randint(-100,100) for x in range(15)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)

#==========================
print("==========================")
print()



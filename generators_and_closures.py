# the iterator as part of a more complex class

class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fib(10):
    print(i)

# lines 2 through 6:
# the class constructor prints a message (this helps to trace the class's behavior),
# prepares some variables (__n to store the series limit, __i to track the current Fibonacci number to provide,
# and __p1 along with __p2 to save the two previous numbers);
#
# lines 8 through 10:
# the __iter__ method is obliged to return the iterator object itself;
# its purpose may be a bit ambiguous here, but try to imagine an object which is not an iterator (e.g., it's a collection of some entities),
# but one of its components is an iterator able to scan the collection;
# the __iter__ method should extract the iterator and entrust it with the execution of the iteration protocol;
# as you can see, the method starts its action by printing a message;
#
# lines 12 through 21:
# the __next__ method is responsible for creating the sequence;
# it's somewhat wordy, but this should make it more readable; first, it prints a message,
# then it updates the number of desired values, and if it reaches the end of the sequence,
# the method breaks the iteration by raising the StopIteration exception; the rest of the code is simple,
# and it precisely reflects the definition we showed you earlier;
#
# lines 24 and 25 make use of the iterator.


#==========================
print("==========================")
print()

# building the iterator into another class

class Fib:
    def __init__(self, nn):
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("Fib iter")
        return self

    def __next__(self):
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret

class Class:
    def __init__(self, n):
        self.__iter = Fib(n)

    def __iter__(self):
        print("Class iter")
        return self.__iter;


object = Class(8)

for i in object:
    print(i)

#==========================
print("==========================")
print()

# closures

# The function returned during the outer() invocation is a closure.

def outer(par):
    loc = par

    def inner():
        return loc
    return inner


var = 1
fun = outer(var)
print(fun())

# the inner() function returns the value of the variable accessible inside its scope,
# as inner() can use any of the entities at the disposal of outer()

# the outer() function returns the inner() function itself; more precisely,
# it returns a copy of the inner() function, the one which was frozen at the moment of outer()'s invocation;
# the frozen function contains its full environment, including the state of all local variables,
# which also means that the value of loc is successfully retained, although outer() ceased to exist a long time ago.

#==========================
print("==========================")
print()

# A closure has to be invoked in exactly the same way in which it has been declared

def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power


fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))


#==========================
print("==========================")

# Key takeaways
#
# 1. An iterator is an object of a class providing at least two methods (not counting the constructor):
#
# __iter__() is invoked once when the iterator is created and returns the iterator's object itself;
# __next__() is invoked to provide the next iteration's value and raises the StopIteration exception when the iteration comes to an end.
#
# 2. The yield statement can be used only inside functions. The yield statement suspends function execution and causes the function to return the yield's argument as a result. Such a function cannot be invoked in a regular way – its only purpose is to be used as a generator (i.e. in a context that requires a series of values, like a for loop.)
#
#
# 3. A conditional expression is an expression built using the if-else operator. For example:
#
# print(True if 0 >= 0 else False)
#
#
# outputs True.
#
#
# 4. A list comprehension becomes a generator when used inside parentheses (used inside brackets, it produces a regular list). For example:
#
# for x in (el * 2 for el in range(5)):
#     print(x)
#
# outputs 02468.
#
#
# 5. A lambda function is a tool for creating anonymous functions. For example:
#
# def foo(x, f):
#     return f(x)
#
# print(foo(9, lambda x: x ** 0.5))
#
#
# outputs 3.0.
#
#
# 6. The map(fun, list) function creates a copy of a list argument, and applies the fun function to all of its elements, returning a generator that provides the new list content element by element. For example:
#
# short_list = ['mython', 'python', 'fell', 'on', 'the', 'floor']
# new_list = list(map(lambda s: s.title(), short_list))
# print(new_list)
#
#
# outputs ['Mython', 'Python', 'Fell', 'On', 'The', 'Floor'].
#
#
# 7. The filter(fun, list) function creates a copy of those list elements, which cause the fun function to return True. The function's result is a generator providing the new list content element by element. For example:
#
# short_list = [1, "Python", -1, "Monty"]
# new_list = list(filter(lambda s: isinstance(s, str), short_list))
# print(new_list)
#
#
# outputs ['Python', 'Monty'].
#
#
# 8. A closure is a technique which allows the storing of values in spite of the fact that the context in which they have been created does not exist anymore. For example:
#
# def tag(tg):
#     tg2 = tg
#     tg2 = tg[0] + '/' + tg[1:]
#
#     def inner(str):
#         return tg + str + tg2
#     return inner
#
#
# b_tag = tag('<b>')
# print(b_tag('Monty Python'))
#
#
# outputs <b>Monty Python</b>


#==========================
print("==========================")

class Vowels:
    def __init__(self):
        self.vow = "aeiouy "  # Yes, we know that y is not always considered a vowel.
        self.pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos == len(self.vow):
            raise StopIteration
        self.pos += 1
        return self.vow[self.pos - 1] # since the pos variable is incremented before the return statement, we need to subtract 1 from it to get the correct index of the vowel to return.


vowels = Vowels()
for v in vowels:
    print(v, end=' ')

print()
#==========================
print("==========================")
print()

any_list = [1, 2, 3, 4]
even_list = list(map(lambda n: n | 1, any_list)) # The map() function applies the lambda function to each element of any_list. The lambda function takes an integer n and performs a bitwise OR operation with 1 (n | 1). This operation sets the least significant (rightmost) binary bit of n to 1, effectively converting any even number to the next odd number while leaving odd numbers unchanged. The result is a new list, even_list, which contains the modified values. n | 1 produces the next odd number for even numbers and keeps odd numbers the same. For example, 2 | 1 results in 3, and 3 | 1 results in 3. The final even_list will be [1, 3, 3, 5].
print(even_list)

#==========================
print("==========================")
print()

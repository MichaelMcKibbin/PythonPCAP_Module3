# The __dict__ attribute of a class instance is a dictionary that contains all the instance variables (attributes) of that instance.

class Classy:
    varia = 1
    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass


obj = Classy()

print(obj.__dict__)
print(Classy.__dict__)

# Output:
# {'var': 2}
# {'__module__': '__main__', '__firstlineno__': 1, 'varia': 1, '__init__': <function Classy.__init__ at 0x000001807A973060>,
#  'method': <function Classy.method at 0x000001807A973110>, '_Classy__hidden': <function Classy.__hidden at 0x000001807A973270>,
#  '__static_attributes__': ('var',), '__dict__': <attribute '__dict__' of 'Classy' objects>,
#  '__weakref__': <attribute '__weakref__' of 'Classy' objects>, '__doc__': None}
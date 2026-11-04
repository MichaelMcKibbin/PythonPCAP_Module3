class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val

    #
    # Fill the constructor with appropriate actions.
    #

class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__counter = 0

    #
    # Present the counter's current value to the world.
    #

    def get_counter(self):
        return self.__counter

    #
    # Do pop and update the counter.
    #

    def pop(self):
        self.__counter += 1
        return Stack.pop(self)


stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())

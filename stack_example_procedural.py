# A small example of a procedural stack implementation in Python using a list.
# A stack is a data structure that follows the Last In First Out (LIFO) principle.

stack = []


def push(val):
    stack.append(val)


def pop():
    val = stack[-1]
    del stack[-1]
    return val


push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())

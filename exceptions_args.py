# args is a tuple designed to gather all arguments passed to the class constructor
# the function to print the contents of the args property in three different cases,
# where the exception of the Exception class is raised in three different ways.


def print_args(args):
    lng = len(args)
    if lng == 0:
        print("")
    elif lng == 1:
        print(args[0])
    else:
        print(str(args))

# case 1: no arguments
try:
    raise Exception
except Exception as e:
    print(e, e.__str__(), sep=' : ' ,end=' : ')
    print_args(e.args)

# case 2: one argument
try:
    raise Exception("one argument")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)

# case 3: multiple arguments
try:
    raise Exception("two", "arguments")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)

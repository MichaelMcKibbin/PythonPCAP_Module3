class Snake:
    def __init__(self, victims=0):
        self.victims = victims

    def increment_victims(self):
        self.victims += 1

snake = Snake(5) #Create the instance before the loop so all five increments apply to the same object.
for i in range(5):
    snake.increment_victims()
print("Victims:", snake.victims)

#
# # What happens if you create a new instance of Snake inside the loop? Each time through the loop, a new instance of Snake is created, and its victims attribute is initialized to 0. Then increment_victims() is called, which increments victims to 1. After the loop, the last instance of Snake created has victims equal to 1, so the output will be:
# for i in range(5):
#   snake = Snake() # Creates a new instance of Snake for each iteration of the loop. victims will always be 1 because each new instance starts with victims = 0 and then increments it by 1.
#   snake.increment_victims()
# print("Victims:", snake.victims)


class Python(Snake):
    pass


print(Python.__name__, 'is a', Snake.__name__)
print(Python.__bases__[0].__name__, 'can be a', Python.__name__)

# Output:
# Victims: 10
# Python is a Snake
# Snake can be a Python

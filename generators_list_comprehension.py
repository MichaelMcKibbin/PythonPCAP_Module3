def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


t = [x for x in powers_of_2(5)]
print(t)

#==========================
print("==========================")
print()

list_1 = []

for ex in range(6):
    list_1.append(10 ** ex)

list_2 = [10 ** ex for ex in range(6)]

print(list_1)
print(list_2)


#==========================
print("==========================")
print()

the_list = []

for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)

print(the_list)

#==========================
print("==========================")
print()

# conditional expression in list comprehension
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
print(the_list)

#==========================
print("==========================")
print()

the_list = []

for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)

print(the_list)


#==========================
print("==========================")
print()

the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

for v in the_list:
    print(v, end=" ")
print()

for v in the_generator:
    print(v, end=" ")
print()

#==========================
print("==========================")
print()



import random

# Generate random numbers between 1,20
rand_list = [random.randint(1, 20) for i in range(1, 11)]

# list_comprehension_below_10 with list comprehension
list_comprehension_below_10 = [i for i in rand_list if i < 10]

# list_comprehension_below_10 with filter
list_comprehension_below_10 = list(filter(lambda x: x < 10, rand_list))

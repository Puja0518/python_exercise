# Generate random number in a list using function
import random
def random_generator(n):
    list_of_random = []
    for i in range(n):
        x = random.randint(1,100)
        list_of_random.append(x)
    return list_of_random

xx = random_generator(20)
print(xx)
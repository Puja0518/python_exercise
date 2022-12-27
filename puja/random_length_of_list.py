# Generate 10 random length of list
import random
def random_generator(n):
    list_of_random = []
    for i in range(n):
        x = random.randint(1,100)
        list_of_random.append(x)
    return list_of_random

for i in range(10):
    # random number of list and size of list is also random
    x = random.randint(5, 15)
    xx = random_generator(x)
    print(f"list - {i} : {xx}")
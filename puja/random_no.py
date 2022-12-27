# Generate random number in a list
import random
list_of_random = []

for i in range(100):
    x = random.randint(10,80)
    list_of_random.append(x)

print(list_of_random)
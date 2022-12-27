import random
def random_generator():
    list_of_random = []
    for i in range(10):
        x = random.randint(1,100)
        list_of_random.append(x)
        # --- if you want to store the reverse number then use slicing
        # x = list_of_random[::-1]
    return list_of_random

def reverse_of_list(list_of_random):
    # ---- if you want to reverse in original list then use reverse function
    list_of_random.reverse()
    return list_of_random

xl = random_generator()
print("xl --",xl)
print(reverse_of_list(xl))


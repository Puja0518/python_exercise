import random
def random_generator():
    random_1 = []
    random_2 = []
    random_3 = []
    random_4 = []
    random_5 = []
    random_6 = []
    random_7 = []
    random_8 = []
    random_9 = []
    random_10 = []
    for i in range(10):
        x = random.randint(1, 100)
        random_1.append(x)
        random_2.append(x)
        random_3.append(x)
        random_4.append(x)
        random_5.append(x)
        random_6.append(x)
        random_7.append(x)
        random_8.append(x)
        random_9.append(x)
        random_10.append(x)
    return random_1, random_2, random_3, random_4, random_5, random_6, random_7, random_8, random_9, random_10
xx = random_generator()
print(xx)


def generate_list(size):
    tmp = []
    for i in range(size):
        x = random.randint(1, 100)
        tmp.append(x)
    return tmp

for i in range(10):
    x = random.randint(5, 15)
    tmp = generate_list(x)
    print(f"list {i} - {tmp}")

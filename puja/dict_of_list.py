# using two list, create dictionary.
fruits = ['Banana', 'kiwi', 'Pomegranate', 'Apple']
nutrition = ['calories', 'immunity', 'fiber', 'Vitamin']

# creating dict using zip method
def dict_of_list(lst1,lst2):
    d = dict(zip(lst1,lst2))
    return d

print(f"new dictionary of two list : {dict_of_list(fruits, nutrition)}")

# creating dict using lambda
res = dict(map(lambda i,j : (i,j) , fruits,nutrition))
print(res)

# creating dict using for loop
def listdictionary(lst1, lst2):

    for i in range(len(lst1)):
        # print(i)
        result = {lst1[i] : lst2[i]}
        print(f"new dictionary of list : {result}")

listdictionary(fruits,nutrition)

tmp = {}
for i in range(len(fruits)):
    tmp[fruits[i]] = nutrition[i]
    # tmp["banana"] = "calories"

print(tmp)
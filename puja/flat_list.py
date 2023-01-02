# Generate a flat list out of a list of list.
list1 = [[20,30,35],[2,4,10,6],[22.8,30,12.6, 8.2],[3,5]]

def complete_list(lst):
    new_list = []
    for i in lst:
        for j in i:
            new_list.append(j)
    return new_list

print(complete_list(list1))

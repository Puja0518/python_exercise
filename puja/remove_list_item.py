list1 = [1, 2, 5, 8, 3, 6]
t = 5

def remove_itm(lst, t):
    for i in lst:
        if i == t:
            lst.remove(i)
    return lst

print(remove_itm(list1, t))
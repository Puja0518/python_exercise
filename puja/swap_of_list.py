# list of 5 element, swap 2nd and 4th element in the list
list1 = [20, 34, 60, 82, 76]
pos1 = 2
pos2 = 4

def swap_element(lst, pos1, pos2):
    temp = lst[pos1], lst[pos2]
    lst[pos2], lst[pos1] = temp
    return lst

print(f"list before swap: {list1}")
swap_element(list1,pos1,pos2)
print(f"list after swap: {list1}")





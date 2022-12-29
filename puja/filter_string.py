# Filter only string from a list of items.
list1 = [2, 'Sun', 6.8, 'Moon', 'Stars', 255]

def filter_str_in_list(lst):
    new_list = []
    for i in list1:
        # print(i)
        if (isinstance(i, str)):
            new_list.append(i)
    return new_list

print(filter_str_in_list(list1))


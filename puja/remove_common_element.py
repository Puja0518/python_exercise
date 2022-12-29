# remove common element from two list.
list1 = [8, 6, 9, 10, 4, 2]
list2 = [3, 7, 1, 4, 8]

def remove_item(list1,list2):
    for i in list1:
        if i in list2:
            list1.remove(i)
            list2.remove(i)
    print(f"list1 : {list1} and list2 : {list2}")

remove_item(list1,list2)
# find the indexs of the items in a list
list1 = [2, 5, 1, 7, 9, 4, 3, 12, 16, 20 ]
x = 12
def index_of_items(lst):
    for i, a in enumerate(list1):
        print(f" index of item {a} : {i}")

def index_of_selected_item(lst, itm):
    x = lst.index(itm)
    print(f"index of item in list : {x}")

def index_of_item(ls):
    for i, a in enumerate(list1):
        if a == 7:
            print(f" index of item : {i}")

index_of_items(list1)
index_of_selected_item(list1, x)
index_of_item(list1)
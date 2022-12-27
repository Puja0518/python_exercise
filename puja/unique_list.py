# find the unique and duplicate items in list
list1 = [1, 3, 8, 4, 3, 2, 4, 8, 9, 6, 7]

def unq_dupl_list(list1):
    dup = []
    unq = []
    for itm in list1:
        c = list1.count(itm)
        if c>1:
            dup.append(itm)
        if c == 1:
            unq.append(itm)
    # print(f" duplicate items : {dup}")
    # print(f" unique items : {unq}")

unq_dupl_list(list1)

# optimal solution

def unique_duplicate_list(list1):
    dup = []
    unq = []
    for itm in list1:
        if itm not in unq:
            unq.append(itm)
        else:
            dup.append(itm)
    print(f" duplicate items : {dup}")
    print(f" unique items : {unq}")

unique_duplicate_list(list1)
# How to find the number of items in a list.
list1 = [6, 8, 12, 15, 3, 18, 7]

# 1st approach
print(f"total number of items in list is : {len(list1)}")

# 2nd approach
count = 0
for i in list1:
    count = count+1
print(f"total number of items in list is : {count}")

# find the sum of items in a list
list1 = [3, 7, 1, 4]
s = 0
print(f"sum of items in a list : {sum(list1)}")

def sum_of_item(lst,sum):
    for i, a in enumerate(lst):
        print(i,a)
        sum = sum + a
    print(f"sum of items in a list : {sum}")

sum_of_item(list1, s)
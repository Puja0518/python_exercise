# find square of each odd number in a given list.

number = [4, 3, 9, 6, 7, 8, 2, 5]
def square_of_odd_no(lst):
    newlist = []
    for i in lst:
        if i % 2 != 0:
            square = i*i
            newlist.append(square)
    return newlist

print(square_of_odd_no(number))
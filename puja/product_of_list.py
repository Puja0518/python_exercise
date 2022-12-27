# find the product of the list of list and store in new list

ls = [[2,8],[6,10],[3,2,5],[4,8,2]]
def product_of_lst(lst):
    new_list = []
    for i in lst:
        product = 1
        for j in i:
            product = product * j
        new_list.append(product)
    return new_list
    # return product

print(product_of_lst(ls))


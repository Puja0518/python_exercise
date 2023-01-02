str = ['Jack','want','to', 'learn', 'swimming']

new_list = []
def longest_word(lst):
    for i in lst:
        c = len(i)
        new_list.append(c)
    x = max(new_list)
    p = new_list.index(x)
    print(lst[p])
    # print(x, new_list)

longest_word(str)


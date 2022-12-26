'''
Given a list of numbers, find the possible list of 2 numbers with a provided sum
'''

s = 7
nums = [1, 6, 4, 7, 2, 8, 9, 3, 2, 4]

def find_list(org_nums, sum):
    for i in org_nums:
        x = sum - i
        if x in org_nums:
            return [i,x]

print(find_list(nums, s))
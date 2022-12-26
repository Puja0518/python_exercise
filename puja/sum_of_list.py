# original
num = [1,4,6,7,2,8]
sum = 6

def sum_of_no(num,sum):
    for i in num:
        for j in num:
            total = i + j
            if total == sum:
                return i , j
                # print(f" sum of {i} + {j} = {total}")

print(sum_of_no(num , sum))

# optimal solution

def sum_of_num(num, sum):
    for i in num:
        x = sum - i
        if x in num:
            return i, x
print(sum_of_num(num, sum))
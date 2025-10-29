#Wap to check if each number in an  list contains duplicate digits, returning true for duplicates and false for unique digits.
#Input: [202,89,112,88]       	Output:[true ,false ,true ,true]

#Sum of all numbers in a matrix.
list1 = [
    [202],
    [89],
    [112],
    [88],
]

for i in list1:
    num = str(i)
    duplicate = False
    for j in num:
        if num.count(j) > 1:
            duplicate = True
            break
    if duplicate == True:
        print("true")
    else:
        print("false")



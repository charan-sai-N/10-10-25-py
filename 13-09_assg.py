

def max_number(list1):
    max_element = list1[0]
    for i in list1:
        if i > max_element:
            max_element = i
    return max_element
list1 = [1, 2, 3, 4, 5, 9, -32, -45]
print("maximum number in the list is: ",max_number(list1))

#output: maximum number in the list is:  9




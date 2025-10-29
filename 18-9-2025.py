#Task :Count the number of swaps performed by bubble sort while sorting an array.
#Apply binary search in only first half of the list. (Search only in first half)

l1=[99,88,70,66,12,123,987,34,90,56,89,34,33,986]
count = 0
for j in range(len(l1)-1):
    for i in range(0,len(l1)-1):
        if l1[i] >= l1[i+1]:
            l1[i] , l1[i+1] = l1[i+1] , l1[i]
            count = count +1
print("iteration count of the list is: ",count)
print(l1)

#printing missing numbers in a given number input=34571 output=26

n=input("enter a number: ")
larger=0
for i in n:
    if int(i) >= int(larger):
        larger = i
for i in range(1,int(larger)):
    if str(i) in n:
        pass
    else:
        print(i , end=" ")

print(" ")

#printing socks pairs#two same color socks makes a pair
list1=['red','green','red','purple','green','black','red']
dict1={}
for i in list1:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] = dict1[i] + 1

for i,j in dict1.items():
    dict1[i]= j // 2
print("valid pair of socks are:",dict1)

 
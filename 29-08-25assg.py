number=int(input("enter a number: "))
print("even numbers in the number are: ")
for i in str(number):
    if int(i)%2==0:
        print(i)
    else:
        pass
prime=[2,3,5,7]
print("prime numbers in the number are: ")
count = 0
for i in str(number):
    if int(i) in prime and count(i) >=1:
        print(i)
    else:
        continue


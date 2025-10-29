print("printing A")
n=5
for i in range(n):#row
    for j in range(n):#column
        if i ==0 or j == 0 or i == n // 2 or j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("printing B")
n=5
for i in range(n):#row
    for j in range(n):#column
        if i ==0 or j == 0 or i == n-1 or i == n // 2 or j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("printing C")
n=5
for i in range(n):#row
    for j in range(n):#column
        if i ==0 or j == 0 or i == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("printing D")
n=5
for i in range(n):#row
    for j in range(n):#column
        if i ==0 or j == 0 or i == n-1 or j == n-1:
            if (i == 0 and j == n-1) or (i==n-1 and j==n-1):
                print(" ",end=" ")
            else:
                print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("printing E")
n=5
for i in range(n):#row
    for j in range(n):#column
        if i ==0 or j == 0 or i == n-1 or i == n // 2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("printing F")
n=5
for i in range(n):#row
    for j in range(n):#column
        if i ==0 or j == 0  or i == n // 2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("printing G")
n=5
mid=n//2
for i in range(n):#row
    for j in range(n):#column
        if i == 0 or i == n - 1 or j == 0 or (j== n//2 and i >= n//2) or (i == n // 2 and j >= n // 2) or (j == n - 1 and i >= n // 2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("printing H")
n=5
for i in range(n):#row
    for j in range(n):#column
        if j == 0 or i == n//2 or j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("printing I")
n=5
for i in range(n):#row
    for j in range(n):#column
        if i == 0 or j==n//2 or i == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("printing J")
n=5
for i in range(n):#row
    for j in range(n):#column
        if i == 0 or j==n//2 or (i == n-1 and j<=n//2) or (j==0 and i>=n/2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("printing k")
n=7
for i in range(n):#row
    for j in range(n):#column
        if j == 0 or i + j == n-4 or (i-3 == j-2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("printing L")
n=7
for i in range(n):#row
    for j in range(n):#column
        if j == 0 or i == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("printing M")
n=7
for i in range(n):#row
    for j in range(n):#column
        if j == 0 or j == n-1 or (i == j and  j < n//2) or (i + j == n-1 and j >= n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("printing N")
n=7
for i in range(n):#row
    for j in range(n):#column
        if j == 0 or j == n-1 or i == j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("printing O")
n=7
for i in range(n):#row
    for j in range(n):#column
        if i ==0 or j == 0 or i == n-1 or j == n-1:
            if (i == 0 and j == n-1) or (i==n-1 and j==n-1) or (j==0 and i==n-1) or (j==0 and i==0):
                print(" ",end=" ")
            else:
                print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("printing P")
n=7
for i in range(n):#row
    for j in range(n):#column
        if j == 0 or i == 0 or i==n//2 or (j==n-1 and i<=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("printing Q")
n=7
for i in range(n):#row
    for j in range(n):#column
        if j == 0 or i == 0 or j==n-1 or i==n-1 or (i == j and i > n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n+1):
    if  i == n:
        print("*",end=" ")
    else:
        print(" ",end=" ")

print()

print("printing R")
n=5
for i in range(n):#row
    for j in range(n):#column
        if j == 0 or i == 0 or i==n//2 or (j==n-1 and i<=n//2) or i==j+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()




print("printing S")
n=5
for i in range(n):#row
    for j in range(n):#column
        if i == 0 or (j == 0 and i<= n//2) or (i == n//2) or (j==n-1 and i>=n//2) or i == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("printing T")
n=5
for i in range(n):#row
    for j in range(n):#column
        if i == 0 or (j==n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("printing U")
n=7
for i in range(n):#row
    for j in range(n):#column
        if j == 0 or i == n-1 or j == n-1:
            if (i == 0 and j == n-1) or (i==n-1 and j==n-1) or (j==0 and i==n-1) or (j==0 and i==0):
                print(" ",end=" ")
            else:
                print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("printing V")
n=5
for i in range(n):#row
    for space in range(i):
        print(" ", end="")
    for j in range(n):#column
        if j == 0 or i + j== n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()



print("printing W")
n=7
for i in range(n):#row
    for j in range(n):#column
        if j == 0 or j == n-1 or (i == j and  j > n//2) or (i + j == n-1 and j <= n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("printing X")
n=7
for i in range(n):#row
    for j in range(n):#column
        if i == j or i + j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("printing Y")
n=7
for i in range(n):#row
    for j in range(n):#column
        if (i == j and j<=n//2) or (i + j == n-1 and i <=n//2) or (j==n//2 and i>=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("printing Z")
n=7
for i in range(n):#row
    for j in range(n):#column
        if i == 0 or i + j == n-1 or i == n-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()



# #'(a+b-c*[e/f])' Remove brackets from string
# #a+b-c*e/f
# #reverse a string  - 4 ways
# #vowel, consonant, spaces count in a string
# input1 = input("enter your equation: ")
# for i in input1:
#     if i in ["[","]","(",")"]:
#         continue
#     else:
#         print(i,end = " ")
# print()
#reversing a string
#method1
n = input("enter a string to reverse it: ")
print("method 1=>",n[::-1])
#method2
reverse = " "
space = " "
for i in n:
    reverse = i + space + reverse
print("method 2=>",reverse)
#method3
print("method 3=>"," ".join(reversed(n)))
#method4
reverse2 = " "
for i in range(len(n) - 1, -1, -1):
    reverse2 += n[i] + space

print("method 4=>",reverse2)

#vowel, consonant, spaces count in a string
string = input("enter a string to count,vowels and spaces and consonant: ")
vowels_count = 0
space_count = 0
consonant_count = 0
for  i in string:
    if i in ["a","e","i","o","u","A","E","I","O","U"]:
        vowels_count += 1
    elif i == " ":
        space_count +=1
    elif i.isalpha():
        consonant_count +=1
print("vowels count = ",vowels_count)
print("spaces count = ",space_count)
print("consonant count = ",consonant_count)




# 1b) palindrome or not and occurences of each digit in a no
a = input("Enter a number or String: ")

if a == a[::-1]:
    print("Palindorme")
else: 
    print("Not a palindrome")
    
for i in set(a):
    print(i, "appears", a.count(str(i)), "times")
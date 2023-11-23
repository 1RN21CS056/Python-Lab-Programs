# 5a) phone no matching with and without regex
import re

def isPhoneNo1(n):
    if(len(n)==12 and n[0:3].isdigit() and n[4:7].isdigit() and n[9:12].isdigit() and n[3] == '-' and n[7] == '-'):
        print("match-isphonenumber")
    else:
        print("no match-isphonenumber")

def isPhoneNo2(n): 
    pattern = ('\d{3}-\d{3}-\d{4}')
    result = re.match(pattern, n)
    if result:
        print("valid-regularExpression")
    else: 
        print("Invalid-regularExpression")
        
n = input("Enter phone no: ")
isPhoneNo1(n)
isPhoneNo2(n)
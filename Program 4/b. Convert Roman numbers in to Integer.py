# 4b) Roman to integers
def roman2Integer(roman_num):
    roman_dict = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    res = 0
    pre_val = 0
    for char in roman_num[::-1]:
        value = roman_dict[char]
        if value >= pre_val:
            res += value
        else:
            res -= value
        pre_val = value
    return res

n = input("Enter roman no: ")
print("Integer val: ", roman2Integer(n))
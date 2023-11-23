# 1a) best of 2 test average
a = int(input("Enter test 1 marks: "))
b = int(input("Enter test 2 marks: "))
c = int(input("Enter test 3 marks: "))

# avgMarks = 0
if a<=b and a<=c:
    avgMarks = (b+c)/2
elif b<=a and b<=c:
    avgMarks = (a+c)/2
else:
    avgMarks = (a+b)/2
    
print("The average of best two test marks: ", avgMarks)
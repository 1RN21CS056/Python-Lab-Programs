# Input: Get the value of n from the user
n = int(input("Enter the value of n: "))

# Check if n is a positive integer
if n <= 0:
    print("Please enter a positive integer.")
else:
    print("The first", n, "natural numbers are:")
    for i in range(1, n + 1):
        print(i, end=" ")

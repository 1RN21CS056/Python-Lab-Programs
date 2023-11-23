
n = int(input("Enter a positive integer n: "))


if n <= 0:
    print("Please enter a positive integer.")
else:

    sum_of_numbers = n * (n + 1) // 2
    average = sum_of_numbers / n

    print(f"Sum of the first {n} natural numbers: {sum_of_numbers}")
    print(f"Average of the first {n} natural numbers: {average}")

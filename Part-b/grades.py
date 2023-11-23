# Function to calculate the letter grade based on the score
def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Function to print the appropriate message based on the grade
def print_message(grade):
    if grade == 'A':
        return "Excellent! You've got an 'A'."
    elif grade == 'B':
        return "Good job! You've got a 'B'."
    elif grade == 'C':
        return "Not bad! You've got a 'C'."
    elif grade == 'D':
        return "You passed,You've got a 'D'."
    else:
        return "Sorry, you've failed. You've got an 'F'."

# Input: Get the student's name and score
name = input("Enter the student's name: ")
score = int(input("Enter the student's score: "))

# Calculate the grade
grade = calculate_grade(score)

# Print the grade and message
print(f"{name},your grade is {grade} ")
print(print_message(grade))

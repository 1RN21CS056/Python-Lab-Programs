import re

pattern = r'[abc]'

input_string = "hello all... my name is Dhanush bhat."

matches = re.findall(pattern, input_string)

# Print the matches
print("Matches found:", matches)

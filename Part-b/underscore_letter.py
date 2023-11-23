import re

pattern = r'\w+'

# Input string
input_string = "Hello World 123 _ underscore"


# Use the re.findall() function to find all matches in the input string
matches = re.findall(pattern, input_string)

# Print the matched substrings
for match in matches:
    print(match)

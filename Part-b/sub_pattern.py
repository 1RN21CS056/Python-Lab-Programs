import re

pattern = r'name'

input_string = "My name is John. Your name is Alice. Her name is Bob."

matches = re.findall(pattern, input_string)

for match in matches:
    print(match)

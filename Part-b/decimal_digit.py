import re
pattern = r'\d'

input_string = "The price of the product is 60.99."

matches = re.findall(pattern, input_string)

print("Decimal digits found:", matches)

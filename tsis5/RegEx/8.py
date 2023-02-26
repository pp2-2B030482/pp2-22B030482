import re

def split_at_uppercase_letters(input_string):
    pattern = r'([A-Z])'
    parts = re.split(pattern, input_string)
    parts = [part for part in parts if part]
    output_string = ' '.join(parts)
    return output_string

input_string = input()
output_string = split_at_uppercase_letters(input_string)
print(output_string)

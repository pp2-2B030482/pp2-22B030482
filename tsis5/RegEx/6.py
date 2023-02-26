import re

def replace_chars_with_colon_regex(input_string):
    pattern = r'[ ,.]'
    output_string = re.sub(pattern, ':', input_string)
    return output_string

input_string = input()
output_string = replace_chars_with_colon_regex(input_string)
print(output_string)

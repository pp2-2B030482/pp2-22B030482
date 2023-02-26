import re

def camel_to_snake_case(input_string):
    pattern = r'(?<!^)(?=[A-Z])'
    output_string = re.sub(pattern, '_', input_string).lower()
    return output_string

input_string = input()
print (camel_to_snake_case(input_string))

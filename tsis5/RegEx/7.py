import re

def snake_to_camel(snake_str):
    pattern = r'_(\w)'
    
    upper = lambda match: match.group(1).upper()

    camel_str = re.sub(pattern, upper, snake_str)
    
    return camel_str

snake_str = input()
camel_str = snake_to_camel(snake_str)
print(camel_str)

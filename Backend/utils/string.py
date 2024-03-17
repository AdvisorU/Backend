import re

def seperate_letter_number(input_string):
    pattern = re.compile(r'(\d+|[a-zA-Z]+)')
    result = ' '.join(pattern.findall(input_string))
    return result

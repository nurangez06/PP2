import re

#1
pattern1 = re.compile(r'a*b')

#2
pattern2 = re.compile(r'a{1}b{2,3}')

#3
pattern3 = re.compile(r'^[a-z]+_[a-z]+$')

#4
pattern4 = re.compile(r'^[A-Z][a-z]+$')

#5
pattern5 = re.compile(r'^a.*b$')

#6
def replace_chars(text):
    return re.sub(r'[ ,.]', ':', text)

#7
def snake_to_camel(text):
    return ''.join(word.capitalize() for word in text.split('_'))

#8
def split_uppercase(text):
    return re.findall('[A-Z][^A-Z]*', text)

#9
def insert_spaces(text):
    return re.sub(r'([A-Z])', r' \1', text).strip()

#10
def camel_to_snake(text):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()

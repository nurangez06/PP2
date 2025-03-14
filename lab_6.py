#Builtin-function
import math
import time
import functools

#1
def multiply_list(lst):
    return functools.reduce(lambda x, y: x * y, lst)

#2
def count_case(s):
    return sum(1 for c in s if c.isupper()), sum(1 for c in s if c.islower())

#3
def is_palindrome(s):
    return s == s[::-1]

#4
def delayed_sqrt(num, delay):
    time.sleep(delay / 1000)
    return f"Square root of {num} after {delay} milliseconds is {math.sqrt(num)}"

#5
def all_true(t):
    return all(t)



#Dir-and-Files

import os
import shutil

#1
def list_files_dirs(path):
    return {
        "directories": [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))],
        "files": [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))],
        "all": os.listdir(path)
    }

#2
def check_access(path):
    return {
        "exists": os.path.exists(path),
        "readable": os.access(path, os.R_OK),
        "writable": os.access(path, os.W_OK),
        "executable": os.access(path, os.X_OK)
    }

#3
def path_info(path):
    if os.path.exists(path):
        return {"filename": os.path.basename(path), "directory": os.path.dirname(path)}
    return "Path does not exist"

#4
def count_lines(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for _ in file)

#5
def write_list_to_file(file_path, lst):
    with open(file_path, 'w') as file:
        file.writelines(f"{item}\n" for item in lst)

#6
def generate_text_files():
    for char in range(65, 91):
        with open(f"{chr(char)}.txt", 'w') as file:
            file.write(f"This is {chr(char)}.txt")

#7
def copy_file(src, dest):
    shutil.copyfile(src, dest)

#8
def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        return "File deleted"
    return "File does not exist or cannot be deleted"

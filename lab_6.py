#Builtin-function
import math
import time
import functools

#1
def multiply_list(lst):
    return functools.reduce(lambda x, y: x * y, lst)
numbers = list(map(int, input("Enter numbers : ").split()))

result = multiply_list(numbers)

print(result)

#2
def count_case(s):
    return sum(1 for c in s if c.isupper()), sum(1 for c in s if c.islower())
text = input("Enter a string: ")
upper_count, lower_count = count_case(text)

print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)


#3
def is_palindrome(s):
    return s == s[::-1]
text = input("Enter a string: ")
print("Is palindrome:", is_palindrome(text))

#4
def delayed_sqrt(num, delay):
    time.sleep(delay / 1000)
    return f"Square root of {num} after {delay} milliseconds is {math.sqrt(num)}"
number = float(input("Enter a number : "))
delay_time = int(input("Enter delay in milliseconds: "))
print(delayed_sqrt(number, delay_time))

#5
def all_true(t):
    return all(t)
values = list(map(int, input("Enter values : ").split()))
print("All values are True:", all_true(values))



#Dir-and-Files

import os
import shutil

# 1. List files and directories in a given path
def list_files_dirs(path):
    files = []
    directories = []
    
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            directories.append(item)
        else:
            files.append(item)
    
    return {
        "directories": directories,
        "files": files,
        "all": os.listdir(path)
    }

# 2. Check if a path exists and its access permissions
def check_access(path):
    return {
        "exists": os.path.exists(path),
        "readable": os.access(path, os.R_OK),
        "writable": os.access(path, os.W_OK),
        "executable": os.access(path, os.X_OK)
    }

# 3. Get filename and directory from a path
def path_info(path):
    if os.path.exists(path):
        return {
            "filename": os.path.basename(path),
            "directory": os.path.dirname(path)
        }
    return "Path does not exist"

# 4. Count the number of lines in a file
def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            return len(file.readlines())
    except FileNotFoundError:
        return "File not found"

# 5. Write a list of items to a file
def write_list_to_file(file_path, lst):
    with open(file_path, 'w') as file:
        for item in lst:
            file.write(f"{item}\n")

# 6. Generate text files from A.txt to Z.txt
def generate_text_files():
    for char in range(ord('A'), ord('Z') + 1):
        with open(f"{chr(char)}.txt", 'w') as file:
            file.write(f"This is {chr(char)}.txt")

# 7. Copy a file from source to destination
def copy_file(src, dest):
    try:
        shutil.copyfile(src, dest)
    except FileNotFoundError:
        return "Source file not found"

# 8. Delete a file if it exists and is writable
def delete_file(path):
    if os.path.exists(path):
        try:
            os.remove(path)
            return "File deleted"
        except PermissionError:
            return "File cannot be deleted (permission denied)"
    return "File does not exist"

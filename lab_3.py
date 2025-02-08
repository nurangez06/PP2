#function
#1
def grams_to_ounes(grams):
    return grams/28.3495231

grams = float(input("Enter grams: "))
ounes = grams_to_ounes(grams)
print(grams, "grams = ", ounes, "ounes")


#2
def fahr_to_celc(f):
    return (5 / 9) * (f - 32)

fahr = float(input("Enter fahrenhit:"))
celc = fahr_to_celc(fahr)
print(fahr, "is equal to", celc, "celcius")


#3
def solve(numheads, numlegs):
    for chik in range (numheads + 1):
        rab = numheads - chik
        if 2 * chik + 4 * rab == numlegs:
            return chik, rab
    return None

numheads = 35
numlegs = 94
puzzle_solution = solve(numheads, numlegs)

if puzzle_solution != None:
    chik, rab = puzzle_solution
    print(chik, "quantity of chikens and ", rab, "rabbits")



#4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

numbers = input("Enter numbers: ").split()
numbers = [int(n) for n in numbers]  
prime_numbers = [n for n in numbers if is_prime(n)]
print("Prime numbers:", prime_numbers)




#5
def permute(s, ans=""):
    if len(s) == 0:
        print(ans)
        return
    for i in range(len(s)):
        new_ans = ans + s[i]
        new_s = s[:i] + s[i + 1:]
        permute(new_s, new_ans)

user_input = input("Enter a string: ")
permute(user_input)



#6
def reverse(s):
    return s[::-1]

s = str(input("Enter a string: "))
poly = reverse(s)
print("Reversed string : ", poly)



#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

print(has_33([1, 3, 3])) 
print(has_33([1, 3, 1, 3]))  
print(has_33([3, 1, 3])) 


#8
def spy_game(nums):
    code = [0, 0, 7]  
    
    for num in nums:
        if num == code[0]:  
            code.pop(0)  
        if not code:  
            return True
    
    return False  

print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))



#9
def sphere_volume(radius):
    return (4/3) * 3.14 * radius**3

radius = float(input("Enter the radius of the sphere: "))
volume = sphere_volume(radius)
print("Volume of the sphere is: ", volume)



#10
def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

numbers = input("Enter numbers separated by spaces: ").split()  
numbers = [int(n) for n in numbers] 
print("Unique elements:", unique_elements(numbers))




#11
def is_palindrome(s):
    s = "".join(s.lower().split())  
    return s == s[::-1]  

text = input("Enter a word: ")
if is_palindrome(text):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")


#12
def histogram(lst):
    for num in lst:
        print('*' * num)

histogram([4, 9, 7])




#13
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    number_to_guess = random.randint(1, 20)
    attempts = 0

    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")

    while True:
        print("Take a guess.")
        try:
            guess = int(input())
            attempts += 1
            
            if guess < number_to_guess:
                print("Your guess is too low.")
            elif guess > number_to_guess:
                print("Your guess is too high.")
            else:
                print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
                break
        except ValueError:
            print("Please enter a valid integer.")

guess_the_number()

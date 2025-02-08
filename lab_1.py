#HOME Intro
print("Hello, world!")

#syntax
if 5 > 2:
    print("Five is greater than two!")
    if 5 > 2:
        print("Five is greater than two!")

#comments (this is a comment)
print("hello, I'm Nura!")

#variables
#1
x = 5     
x = "Nura"
print(x)

#2 Variables do not need to be declared with any particular type
x = str(3)    
y = int(3)   
z = float(3)
print(type(x)) 
print(type(y))
print(type(z))

#3
x = "Python"
y = "is"
z = "awesome"
print(x + y + z)

#4 create a variable outside of function
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


#data types
#examples: str(text), int(num), float(num), bool(true/false), list(sequence), tuplel(sequence), set, bytes etc.

#numbers
x = 5 #int type
y = 3.14 #float type
z = 1e #complex type "e" is indicatin power of 10 
print(type(x))
print(type(y))
print(type(z))

#castin 
x = int(5)
Y = float(3.14
z = str("hello!"))

#strings
a = str("Hello, World!")
print(a[0:-1]) 
print(a.lower())
print(a.replace("H", "J"))
print(a.split(","))
#format string
age = 18
text = f"My name is Nura, and I'm {age}"
print(text)

#booleans
print(100 >1)
print(100 < 1)
print(100 == 1)

#1
a = 200
b = 199

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

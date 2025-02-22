#Python DATETIME
#1
from datetime import datetime, timedelta

today = datetime.today()

new_date = today - timedelta(days=5)

print("Today is : ", today)
print("Date 5 days ago : ",new_date)

#2
from datetime import datetime, timedelta

today = datetime.today()

yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday was : ", yesterday)
print("Today is : ", today)
print("Tommorow is : ", tomorrow)

#3
import datetime

today = datetime.datetime.now()

print("Microseconds : ", today.strftime("%f"))

#4



#Python MATH
#1
import math

def degree_to_radian(degree):
    return degree * (math.pi / 180)

degree = float(input("Input degrees : "))
radian = degree_to_radian(degree)
print("Output radians : ", radian)

#2
import math
def trapez(a, b, h):
    area = ((a + b) / 2) * h
    return area

h = float(input("Hight : "))
a = float(input("Base, first value : "))
b = float(input("Base, second value : "))
area = trapez(a, b, h)
print("Expected Output : ", area)

#3
import math
def apothem(n, s):
    return s / (2 * math.tan(math.radians(180/n)))

def area(n, s, a):
    return (n * s * a) / 2

n = int(input("Input number of sides : "))
s = int(input("Input the length of a side : "))
a = apothem(n, s)
ar = area(n, s, a)
print("The area of the polygon is : ", ar) 

#4
import math
def parallelogram(b, h):
    return b * h

b = int(input("Length of base : "))
h = int(input("Height of parallelogram : "))
area = parallelogram(b, h)
print("Expected Output : ", area)



#GENERATORS Python
#1
def square_generator(N):
    for i in range(N + 1):
        yield i * i

gen = square_generator(5)

for square in gen:
    print(square)

#2
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter a number: "))
print(",".join(map(str, even_numbers(n))))


#3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a number: "))
for num in divisible_by_3_and_4(n):
    print(num, end=" ")


#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

a, b = map(int, input("Enter two numbers (a b): ").split())
for sq in squares(a, b):
    print(sq)

#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Enter a number: "))
for num in countdown(n):
    print(num, end=" ")

#1
a = 100
b = 99

if b > a:
  print("The numder b is greater than a")
else:
  print("The number b is not greater than a")

#2
x = "Hello World!!"
y = 2025

print(bool(x))
print(bool(y))

#3
#operator
#output is 350 & Correct!
a = 10
b = 34
print(a + b * (a))

if b != a :
    print("Correct!")

#4
#lists
#create list, add/remove to the list, quantity of items in the list, list type

myshopinglist = ["banana", "apples", "bread", "chocolate", "milk"]
myshopinglist.append("cheese") #add cheese at the end
myshopinglist.insert(0, "soap") #add soap in the begining
myshopinglist.pop(3) #remove 'bread'
print(len(myshopinglist))
print(myshopinglist)
print(type(myshopinglist))

myshopinglist.clear()  #clear the list content
print(myshopinglist)

#5
#loop in list
#prints every item from list separetly
mylist = ["banana", "apples", "bread", "chocolate", "milk"]
i = 0
while i < len(mylist):
  print(mylist[i])
  i = i + 1

myshopingbag = []
#create new list and copy items from first list
for i in mylist:
  if "a" in i:
    myshopingbag.append(i)

print(myshopingbag) 

#6
#tupels

mytuple = ("apple", "banana", "cherry", "apple", "cherry")
print(mytuple[:3]) #prints first four items


#7
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits #use * to print only red fruits 

print(green)
print(yellow)
print(red)

for i in range(len(fruits)):  #prints items by referring number
  print(fruits[i])

#8
#sets

my1set = {"apple", "banana", "cherry", "strawbery"}
print("banana" in my1set) #cheks if banana is present in set

my1set.add("orange")
my1set.discard("cherry")

for x in my1set:
    print(x)

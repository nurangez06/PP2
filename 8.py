fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits #use * to print only red fruits 

print(green)
print(yellow)
print(red)

for i in range(len(fruits)):  #prints items by referring number
  print(fruits[i])
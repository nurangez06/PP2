#tupels

mytuple = ("apple", "banana", "cherry", "apple", "cherry")
#print(mytuple[:3]) #prints first four items

x = list(mytuple)
x.append("kiwi")
mytuple = tuple(x)
print(mytuple)
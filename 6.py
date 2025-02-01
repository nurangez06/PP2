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
myshopingbag.sort() #sorting list alphabeticly
print(myshopingbag) 

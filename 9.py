#sets

my1set = {"apple", "banana", "cherry", "strawbery"}
print("banana" in my1set) #cheks if banana is present in set

my1set.add("orange")
my1set.discard("cherry")

for x in my1set:
    print(x)
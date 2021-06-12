
list1 = ["first", "second", "third", "fourth", "fifth"]

for item in list1:
	print(item)

print(enumerate(list1))


############

# Python program to illustrate
# enumerate function in loops
 
# printing the tuples in object directly
for element in enumerate(list1):
    print (element)

# changing index and printing separately
for index, element in enumerate(list1,100):
    print (index, element)

for index, element in enumerate(list1):
 	print("index: ", index, "; item: ", element)

listOfNumbers = [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
sum = 0
for currentNumber in listOfNumbers:
	sum += currentNumber
print(sum / len(listOfNumbers))

myString = "There are seven words in this string."
numSpaces = 0
for currentChar in myString:
	if currentChar == " ":
		numSpaces += 1
print("There are " + str(numSpaces) + " spaces in this string." )
print("There are " + str(numSpaces + 1) + " words in this string. \n \n" )



i = 1
while i < 11:
	print(i)
	i += 3
print("\n \n")

count = 0
for x in range(3):
	for y in range(3):
		count = count + y



list1 = ["leoc", "ser", "jamecho", "nairo"]
list2 = ["nairo", "oliva", "ser", "rafa"]

for name1 in list1:
	for name2 in list2:
		if name1 == name2:
			print(name1, end = " ")

x = 3
print(x, end = " ")
print("\n")

listExample = {'Ser': 4198, 'Leoc': 4658, 'Jamecho': 7656}
for name, phone in listExample.items():
	print("{0:10} ==> {1:10d}".format(name, phone))

x1 = "Serg"
name2 = "Leoc"
dog = "Jamecho"
print('The story of {0}, {1}, {2} and {other}.'.format('Nairo', name2, x1, other='Klaus'))

print("X", "Y", "Z", sep = "#", end = "?")
print("I", "J", "K", sep = "%", end = "!")

print("")
print(100//21)
print("==")

words = ["dog", "sparrow", "cat", "frog"]
#words = [""]

for word in words:
	try:
		print(word.index("o"))
	except:
		print("not found")

myList1 = ["One", "Two", "Three"]
myList2 = myList1
myList1.append("Four")

print("myList1: ", myList1)
print("myList2: ", myList2)

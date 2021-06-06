myInt1 = 21
myInt2 = 34
myInt3 = 56

outputFile = open("output.txt","w")

outputFile.write(str(myInt1) + "\n")
outputFile.write(str(myInt2) + "\n")
outputFile.write(str(myInt3) + "\n")

outputFile.close()

myList1 = ["Ser", "leoc", "jamecho", "tiche", "obam", "ampar", "marra", "oliv"]

outputFile = open("output.txt", "w")
outputFile.write("\n".join(myList1))
outputFile.close()

outputFile = open("output.txt", "w")
for name in myList1:
	outputFile.write(name + "\n")
outputFile.close()

outputFile = open("output.txt", "a")
for i in range(1,9):
	print(i, file = outputFile)
outputFile.close()

outputFile = open("output.txt", "r")
print(outputFile.readline().strip())
outputFile.close()

#Read a file and load it in a list
myList2 = []
inputFile = open("output.txt", "r")
for line in inputFile:
	myList2.append(line.strip())

print(myList2)
inputFile.close()

#functions save and load
def save(filename1, inList1):
	outputFile = open(filename1, "w")

	for item in inList1:
		print(item, file = outputFile)

	outputFile.close()

def load(filename1):
	inputFile = open(filename1, "r")
	inList1 =[]

	for line in inputFile:
		inList1.append(line.strip())
	inputFile.close()
	return inList1

myList3 = ["jamecho", "tiche", "maria", "marrana1", "marrana2", "nairo", "lorenza", "pastora"]
save("newoutput1.txt", myList3)
myList4 = load("newoutput1.txt")
print(myList4)





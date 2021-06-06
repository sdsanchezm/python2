myString = "ABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDE"
findString = "DEA"

currentLocation = myString.find(findString)

while currentLocation >= 0:
	print(findString, "found at", currentLocation)
	currentLocation = myString.find(findString, currentLocation + 1)


myString = "ABCDEABCDE"
print(myString.find("CDE")) 
print(myString.find("CDE", 5)) 
print(myString.find("CDE", 13)) 
print(myString.find("CDE", 4, 10)) 
print(myString.find("CDE", 3, 6)) 

myWord = "du blutest fur. mein Seelenheil Ein kleiner. Schnitt und du wirst geil"
print(myWord.split())
print(myWord.split(". "))

print(myWord)
print(myWord.capitalize()) #Mayusculas
print(myWord.lower()) #letras minusculas
print(myWord.upper()) #letras mayusculas
print(myWord.title()) #letras 
print(myWord.strip()) #letras 
print(myWord.replace("fur", "MUR")) #reemplazo de una palabra

myList = myWord.split() #divide una palabra y la almacena en una lista
print(myList)
myListJoined = "-".join(myList)
print(myListJoined) #junta las palabras nuevamente
print(myWord)

myString = "Hallo Welt!"
myFloat = 21.45
myInt = 12
myChar = "T"
myInt2 = -6

myTuple = (myString, myFloat, myInt, myChar, myInt2)
print(myTuple)

(myNewString, myNewFloat, myNewInt, myNewChar, myNewInt2) = myTuple
print(myTuple)

print(myNewString, myNewFloat, myNewInt, myNewChar, myNewInt2)







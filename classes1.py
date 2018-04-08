class Person:

	def __init__(self):
		self.firstName = "noName"
		self.lastName = "naLasName"
		self.age = "noAge"
		self.eyeColor = "eyeColor"

#Se puede definir una clase por heriencia, osea a partir de otra:

class Name:
	def __init__(self):
		self.firstName = "NoName"
		self.lastName = "NoLastName"

class Person2:
	def __init__(self):
		self.name = Name()
		self.age = "noAge"
		self.eyeColor = "eyeColor"

myPerson = Person2()
print(myPerson.name.firstName)
myPerson.name.firstName = "Jamecho"
print(myPerson.name.firstName)
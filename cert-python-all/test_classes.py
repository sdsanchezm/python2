class stk():
	def __init__(self): #this is the constructor
		self.__num = 0 # this is encapsulated, not accessible to public (or private)
		self.kex = 21 # this is public
		self.stack1 = [] #this is the stack (or the list that we are using now)

	def push(self, val1): #this is a method
		self.stack1.append(val1)

	def pop(self): # this is another method
		delval = self.stack1[-1]
		#self.stack1.pop(-1)
		del self.stack1[-1]
		return delval

k1 = stk()
k1.push(2)
k1.push(4)
k1.push(6)
print("lenght: ", len(k1.stack1))
print(k1.pop())
print(k1.pop())
print(k1.pop())
print(k1.kex)

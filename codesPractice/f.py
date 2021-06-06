

f=open("test2.txt", 'w')
text = "This is just a python text file - And another line"
#text = f.read()
f.write(text)
f.close()

def fibo(n):
	if n <= 1:
		return n
	else:
		return fibo(n-1) + fibo(n-2)
		
print(fibo(6))
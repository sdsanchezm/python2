#test1
x = [1,2]
x.insert(1,x[1])
print(x)

y = x

print(y)

y.insert(1,6)
print(x)
print(y)

l1 = [1,2]
for v in range(2):
	l1.insert( 1,l1[v])
print(l1)

x.insert(9,7)
print(x)


print(10//4)

print(2**3)

def func(a,b):
	return b ** a

#print(func(b=5,2))

z = 0
y = 10
x = y < z and z > y or y > z and z < y
print(x)

list =  [x*x for x in range(5)]
def fun(L):
    del L[L[2]]
    return L

print(fun(list))


a = 1
b = 2
c = 0
a, a = a, b
print(a)

print(2 ^ 2)
print("===")
a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b
print(a,b)

def fun(x):
    if x % 2 == 0:
    	return 1
    else:
    	return 2

print(fun(fun(2)))

nums = [1,2,3]
vals = nums
del vals[:]

print(1%2)
print(2%1)

print("a","b","c",sep="sep")

print(1 // 2 + 1 / 5 )

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2])

print(4 ** (1/2))

dct = { 'one':'two', 'three':'one', 'two':'three' }
v = dct['three']
for k in range(len(dct)):
    v = dct[v]
print(v)

L = [i for i in range(-1,-2)]
print(L)

def a1(a, b, c=1):
	return a + b + c

print( a1( 1,2,3) )

print( 5 % 2 )

for i in range(0):
	print(i)
else:
	print("#")


x = 1
print(x)
x = x << 1
print(x)
x = x << 1
print(x)
x = x << 1
print(x)
x = x << 1
print(x)

x = y < z and z > y or y > z and z < y
print(x)

print( 1 ^ 0)

list1 = [1, 2, 3, 4]
print(list1[-3 : -2])
list1[0], list1[2] = list1[2], list1[0]

print(list1)
del list1[1]

print(list1)
list2 = list1
print(list2)
del list2[1]
print(list1)

list1 = [1, 2, 3, 4, 5]

list3 = list1[-1: -2]

print(list1)
print(list3)


l1 = [1,2,3]
for v in range(len(l1)):
	l1.insert(1,l1[v])
print(l1)

XX = [i for i in range(-1,2)]
print(XX)


T = [[3-i for i in range (3)] for j in range (3)]
s = 0
for i in range(3):
    s += T[i][i]
print(s)

def f1(x=10):
	return x

print(f1())

def ff1(x):
	if x == 0:
		return 0
	return x + ff1(x - 1)

print(ff1(3))


# Check lists and this thing theory because hmm no idea...
dct = { }
lst = ['a','b','c','d']
for i in range(len(lst)):
    dct[lst[i]] = ( lst[i], )
for i in sorted(dct.keys()):
    k = dct[i]
    print(k[0])


def ff2(a, b):
	return a ** a

print(ff2(2,1))


x = 1
F = None


def fun(x):
    if x % 2 == 0:
    	return 1
    else:
    	return 4

print(fun(fun(2)) + 1)

# Double check the global type 
def fun(x):
    global y
    y = x * x
    return y

fun(2)
print(y)


def any():
    print(var + 1,end='')
var = 1
any()
print(var)

# Revise tuples
my_tuple = ('p','e','r','m','i','t')
# my_tuple[1] = my_tuple[1] + my_tuple[0]


# check lists theory 
list =  ['Mary', 'had', 'a', 'little', 'lamb']
#def list(L):
	#del L[3]
	#L[3] = 'ram'
print(list)



def fun(x,y,z):
	#return z
    return x+2*y+3*z

print(fun(0,z=1,y=3))


dct = { 'one':'two', 'three':'one', 'two':'three' }
v = dct['one']
for k in range(len(dct)):
    v = dct[v]
print(v)



tup = (1, 2, 4, 8)
print(tup)
tup = tup[1: -1]
print("this",tup)
tup = tup[0]
print(tup)











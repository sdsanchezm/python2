import math
import statistics
from functools import reduce

# Function map: mainly evaluate several times a function ie. taking arguments from a list or tuple
print("*********************map***************************************")
def areaFunction(r):
    ''' to calcle the area of circle with radius r'''
    return math.pi * (r**2)

radiusList = [2, 5, 7, 11, 0.3, 10]

#Method 1: direct method: calculate every radius

areas = []
for r in radiusList:
    a = areaFunction(r)
    areas.append(a)

print(areas)
#Method 2: Single line of code: map function

print(map(areaFunction, radiusList)) #first argument: function, and the other is a list

list(map(areaFunction, radiusList))

tuple1 = [("Berlin", 21), ("Cairo", 42), ("Winnipeg", 56), ("New York", 67), ("Toronto", 10)]

def Celsius_to_Farenheit(Tc):
    return (Tc[0], (9/5) * float(Tc[1]) + 32)

Celsius_to_Farenheit_lambda = lambda data: (data[0], 9/5 * data[1] + 32)

print( list( map( Celsius_to_Farenheit_lambda, tuple1 ) ) )
print( list( map( Celsius_to_Farenheit, tuple1 ) ) )

print( tuple1[0][1] )

#************************************************************88
# function filter: 
print("#*********************filter***************************************")

data1 = [1.3, 2.6, 2.1, 3.7, 5.3, -4.2]
avg = statistics.mean(data1)
print(avg)

print( list( filter( lambda x: x > avg, data1 ) ) ) 
print( list( filter( lambda x: x < avg, data1 ) ) ) 

# False values in python: "", 0, 0.0, 0j, [], (), {}, False, None 

# Example 2: removing missing data 

countries = ["", "", "Colombia", "Canada", "", "Germany", "Australia", "", "Sweden", "Brazil"]
print( list( filter(None, countries) ) )


#************************************************************88
# function reduce: reduce function takes the result pof the previous value to evaluate the function, until it finish the list (or sequence of data)
print("#*********************reduce***************************************")

data1 = [2, 3, 4, 6, 11, 12, 17, 19, 24, 27]
multiply1 = lambda x, y: x * y
print( reduce(multiply1, data1) )

def multiply2(data1):
    product1 = 1
    for x in data1:
        product1 = product1 * x
    return product1

print( multiply2(data1) )




print(" \n \n \n ***************lambda*************************") # ****************************************

########### lambda functions (anonymous expresision, online 1 line, NOT-Multiline)
# Standar Approach to evaluate this function: 2x + 5

def func1(x):
    return 2 * x + 5

print(func1(3))

func_lambda1 = lambda x: 2 * x + 5
print(func_lambda1(3))

full_name_corrected = lambda firstname, secondname: firstname.strip().title() + " " + secondname.strip().title()

print(full_name_corrected("    jaMEcho       ", "  sAncheZ"))

book_authors = ["PauLo CoelhO", "andres Caicedo", "Mario Mendoza", "Peter DrucKer", "NicoLa tesla", "Steve Jobs", "Zara Leander"]

'''
help(book_authors)
help(book_authors.sort)
'''

book_authors.sort( key = lambda name: name.split(" ")[-1].upper() )

print(book_authors)

# Quadratic expression using lambda: 

def quadratic_function1(a, b, c):
    return lambda x: a * x ** 2 + b * x + c

func2 = quadratic_function1(2, 4, -2)
print( func2(0) )
print( func2(1) )
print( func2(2) )

print( quadratic_function1(2, 0, -1)(2) )











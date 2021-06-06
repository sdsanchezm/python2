print("Hello")

for x in ["ser", "dav", "leoc", "jamecho"]:
    print(x)

myString = "This is not a numer!"

try:
    print("Converting the string to int...")
    myInt = int(myString)
    print(myInt)

except:
    pass
print("Done!")

try:
    myVar = 1/0
    print("An error ocurred!")
except:
    pass
print("Done!")

try:
    print(1/0)
    print("Noerror occurred")
except ZeroDivisionError:
    print("An error occurred")
print("done!==")

try:
    print(1/0)
    print("Noerror occurred!!!")
except NameError:
    print("A NameError occurred!!!")
except ZeroDivisionError:
    print("A Zero division Error occurred!!!")
print("Done!==")

myString = "this string is not a number"

try:
    print("Converting myString to int...")
    print("String" + 1 + ": " + myString)
    myInt = int(myString)
    print(myInt)
    print(1/0)

except ValueError as error:
    print(error)

except TypeError as error:
    print(error)
print("done!==")


myString = "1"
try:
    print("Converting myString to int...")
    myInt = int(myString)
    print(myInt)

except (ValueError, TypeError) as error:
    print("a ValueError or TypeError occurred.")

except Exception as error:
    print("Some other type of error occurred.")
else:
    print("No Errors occurred!")
print("Done!==")


try:
    d1 = int(input("Ingrese dividendo: "))
    d2 = int(input("Ingrese divisor: "))
    divisionX = d1 / d2
    print("la division es: ", divisionX)
except ZeroDivisionError:
    print("No se puede dividir por cero!")
print("Done!==")

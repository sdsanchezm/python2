try:
    inputFile = open("InputFile.txt", mode = "r")

except IOError as error:
    print("An input error has occurred!!!")
else:
        for line in inputFile:
            print(line)
        print("No errors ocurred!!!")
finally:
    inputFile.close()


try:
    d1 = int(input("Enter dividend: "))
    d2 = int(input("Enter divisor: "))
    quo = d1 / d2
    print("Result: ", quo)
except ZeroDivisionError:
    print("No se puede dividir por cero!!!")
except ValueError:
    print("Eso fue un ValueError!!!")
finally:
    print("Done!!!")

try:
    inputFile = open("Inputfile2.txt", mode = "r")

    for line in inputFile:
        try:
            print(int(line))
        except ValueError as error:
            print("A ValueError has occured bro!!!")
        else:
            print("No errors has occurred bro!!!")
    inputFile.close()

except IOError as error:
    print("An IOError has ocurred bro!!!")



def function_dec(func):
    def function_interior(*args): # *args se agrega para que reciba argumentos
        print('begin')
        func(*args) # *args se agrega aca tambien
        print('end')

    return function_interior



@function_dec
def suma(A, B, C):
    print(A + B + C)

@function_dec
def resta(A, B):
    print(A - B)



if __name__ == '__main__':
    suma(10, 11, 10)
    resta(14, 5)
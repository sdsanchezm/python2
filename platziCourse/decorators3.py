def function_dec(func):
    def function_interior(*args, **kwargs): # *args se agrega para que reciba argumentos
        print('begin')
        func(*args, **kwargs) # *args se agrega aca tambien
        print('end')

    return function_interior

@function_dec
def suma(A, B, C):
    print(A + B + C)

@function_dec
def resta(A, B):
    print(A - B)


def potencia(base, exponente):
    print(pow(base,exponente))

if __name__ == '__main__':
    suma(10, 11, 10)
    resta(14, 5)
    potencia(base=5,exponente=3)
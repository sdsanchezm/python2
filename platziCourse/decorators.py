

def function_dec(func):
    def function_interior():
        print('begin')
        func()
        print('end')

    return function_interior



@function_dec
def suma():
    print(1+1)

@function_dec
def resta():
    print(5-2)



if __name__ == '__main__':
    suma()
    resta()
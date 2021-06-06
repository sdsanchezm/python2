# -*- coding: utf-8 -*-

def function_decorator(func):
    def function_internal(password_1):

        if password_1 == 'platzi':
            return func()
        else:
            return print('incorrect password')
    
    return function_internal

@function_decorator
def check_password():
    print("password correct")


if __name__ == '__main__':
    password1 = str( input( ' type your password ' ) )

    check_password(password1)

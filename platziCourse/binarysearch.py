# -*- coding: utf-8 -*-

def binary_search(numbers, number_to_find, startIndex, endIndex):
    if endIndex < startIndex:
        return False
    
    midNumber = int( ( startIndex + endIndex ) / 2 )

    if numbers[midNumber] == number_to_find:
        return True

    if numbers[ midNumber ] > number_to_find:
        return binary_search(numbers, number_to_find, startIndex, midNumber - 1 )
    else:
        return binary_search(numbers, number_to_find, midNumber + 1, endIndex )


if __name__ == '__main__':
    numbers = [1, 3, 4, 5, 6, 8, 10, 11, 21, 25, 28, 31, 44, 45]
    number_to_find = int( input( "Enter a number to find: " ) )
    result = binary_search(numbers, number_to_find, 0, len( numbers ) - 1)
    if result:
        print('Yes, it is on the list')
    else: 
        print('No, is not on the list')
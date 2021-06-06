"""
"abacabad" c
"adacabaabacabad" _
"abcdefghijklmnoprqstwvuwxyz" d
"bccccccccccccccccyb" y
"""

def first_not_repeating_char(char_seq):
    seen_letters = {}
    for index, letter in enumerate(char_seq):
        # print('index: {}; letters: {}'.format(index, letter))
        if letter not in seen_letters:
            seen_letters[letter] = (index, 1)
        else:
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1)

    # this data structure is like this:
    # "abacabad"
    # {
    #     'a': (0,4),
    #     'b': (1,2),
    #     'c': (3,1)
    # }
    
    final_letters = []
    for key, value in seen_letters.items():
        if value[1] == 1:
            final_letters.append( (key, value[0]) )

    # this data structure, final_letters looks like this:
    # [('a', 0), ('d', 7)]

    not_repeated_letters = sorted( final_letters, key = lambda value: value[1] )

    if not_repeated_letters:
        return not_repeated_letters[0][0]
    else:
        return '_'

    # esto reemplazari a la funcion lambda: 
    # def sort_order(value):
    #     return value[1]

if __name__ == '__main__':
    char_seq = str( input( "Please write your text: " ) )

    result = first_not_repeating_char( char_seq )

    if result == '_':
        print("No repeated chars")
    else:
        print("The first non repeated char is {}".format(result))


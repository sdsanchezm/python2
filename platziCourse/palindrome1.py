word1 = str( input() )

def pal1(word):
    reversed_letters = []

    for letter in word:
        reversed_letters.insert(0, letter)

    reversed_word = ''.join(reversed_letters)

    print( reversed_word )

pal1( word1 )
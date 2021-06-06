import random

IMAGES = ['''
      _______
    |/      |
    |      
    |      
    |       
    |      
    |
   _|___ ''', '''

      _______
    |/      |
    |      (_)
    |      
    |     
    |      
    |
   _|___ ''', '''

      _______
    |/      |
    |      (_)
    |       |
    |      
    |      
    |
   _|___ ''', '''

      _______
    |/      |
    |      (_)
    |      \|
    |      
    |      
    |
   _|___ ''', '''

      _______
    |/      |
    |      (_)
    |      \|/
    |      
    |      
    |
   _|___ ''', '''

      _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |      
    |
   _|___ ''', '''
      _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |      / 
    |
   _|___ ''', '''
      _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |      / \\
    |
   _|___ '''

]

WORDS = [
    'lavadora',
    'secadora',
    'xilofono',
    'keyboard',
    'car',
    'casa',
    'apartamento'
]

def random_word():
    index = random.randint(0, len(WORDS) - 1)
    return WORDS[index]

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('---*---*---*---*---')

def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str( input("Please type a letter: ") )

        index_list = []
        for index in range( len( word ) ):
            if word[index] == current_letter:
                index_list.append(index)
        
        if len( index_list ) == 0:
            tries += 1

        if tries == 7:
            display_board(hidden_word, tries)
            print('You Lose!')
            print('the correct word is {}'.format(word))
            break

        else:
            for index in index_list:
                hidden_word[index] = current_letter

            # this is a way to finish the program, the video shows the try except method which is also valid
            # if ''.join(hidden_word) == word:
            #     print('You Won, congratulations! XD')
            #     break

            index_list = []

        try:
            hidden_word.index('-')
        except ValueError:
            print('/n You won, congratulations!')
            break


if __name__ == '__main__':
    print('WELCOME-TO-THISGAME')
    run()


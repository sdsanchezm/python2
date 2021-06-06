class Lamp: #siempre se inicia con mayus, por buena practica de notacion

        _LAMPS = [
            '''
         |
 \     _____     /
     /      \\
-   ( ))))))) )   -
     \ \   / /
      \|___|/
  /    |___|    
       |___| -on
            ''',
            '''         
      _____     
     /      \\
    ( ))))))) )   
     \ \   / /
      \|___|/
       |___|    
       |___| -off
            '''
        ]        

        def __init__(self):
            self._is_turn_on_ = False

        def turnOn(self):
            self._is_turn_on_ = True
            self._display_image()

        def turnOff(self):
            self._is_turn_on_ = False
            self._display_image()

        def _display_image(self):
            if self._is_turn_on_ == True:
                print(self._LAMPS[0])
            else:
                print(self._LAMPS[1])

def run():
    Lamp1 = Lamp()
    while True:

        option = str( input('''     
        Please enter your option: 

        [P]render - [A]pagar  - [S]alir
        
        ''') ).lower()

        if option == 'a':
            Lamp1.turnOff()
        if option == 's':
            break
        if option == 'p':
            Lamp1.turnOn()
        else:
            print('invalid option \n')

if __name__ == '__main__':
    run()

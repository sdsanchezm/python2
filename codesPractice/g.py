cont = 0
for i in range(4):
    for j in range(4):
        print(" ", str(cont), " ", end="")
        cont += 1
    print("\n")

cont = 0
for i in range(4):
    for j in range(4):
        print(' {0:2} '.format(cont), end="")
        cont += 1
    print(' | {0:14} | {1:14.2f} | {2:<14.5f} |'.format('posicion:', i, j))
    #print('\n  {0:9} {}'.format('posicion ',i))

import math
print(math.sqrt(16))

from math import sqrt
print(sqrt(49))
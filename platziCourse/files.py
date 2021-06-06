# -*- coding: UTF-8 -*-
from weakref import finalize


def run():
    count = 0
    # with open('numeros.txt', 'w') as f:
    #     for i in range(10):
    #         f.write(str(i))

        # try:
        #     f.open()
        # finally:
        #     f.close()


    # with open( 'aleph.txt', 'r' ) as f:
    #     for line in f:
    #         print(line)


    # with open( 'aleph.txt', 'w' ) as f:
    #     for i in range(5):
    #         print('hello')

        # with open('aleph.txt', encoding='utf-8') as f:
        #     print(f.readlines())

    with open('aleph.txt', encoding='utf-8') as f:
        for line in f:
            count += line.count('Beatriz')

    print(count)

if __name__ == '__main__':
    run()
def for_v():
        """ Lower case Alphabet letter 'v' pattern using Python for loop"""

        for row in range(4):
                for col in range(8):
                        if row-col==0 or row+col==6:
                                print('*', end = '')
                        else:
                                print(' ', end = '')
                print()


def while_v():
        """ Lower case Alphabet letter 'v' pattern using Python  while loop"""

        row = 0
        while row<4:
                col = 0
                while col<8:
                        if row-col==0 or row+col==6:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1


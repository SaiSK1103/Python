def for_K():
        """ Upper case Alphabet letter 'K' using for loop"""

        for row in range(6):
                for col in range(4):
                        if col==0 or row+col==3 or row-col==2:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_K():
        """ Upper case Alphabet letter 'K' using while loop"""

        row = 0
        while row<6:
                col = 0
                while col<4:
                        if col==0 or row+col==3 or row-col==2:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

def for_Y():
        """ Upper case Alphabet letter 'Y' pattern using Python for loop"""

        for row in range(7):
                for col in range(7):
                        if col==3 and row>2 or (row-col==0 or row+col==6) and row<3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_Y():
        """ Upper case Alphabet letter 'Y' pattern using Python while loop"""

        row = 0
        while row<7:
                col = 0
                while col<7:
                        if col==3 and row>2 or (row-col==0 or row+col==6) and row<3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

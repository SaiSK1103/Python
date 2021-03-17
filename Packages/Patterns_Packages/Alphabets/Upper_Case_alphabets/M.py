def for_M():
        """ Upper case Alphabet letter 'M' pattern using Python Python for loop"""

        for row in range(6):
                for col in range(5):
                        if col in (0,4) or (row-col==0 or row+col==4) and row<3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_M():
        """ Upper case Alphabet letter 'M' pattern using Python Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<5:
                        if col in (0,4) or (row-col==0 or row+col==4) and row<3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

def for_N():
        """ Upper case Alphabet letter 'N' pattern using Python Python for loop"""

        for row in range(5):
                for col in range(5):
                        if col in (0,4) or row-col==0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')

                print()


def while_N():
        """ Upper case Alphabet letter 'N' pattern using Python Python while loop"""

        row = 0
        while row<5:
                col = 0
                while col<5:
                        if col in (0,4) or row-col==0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

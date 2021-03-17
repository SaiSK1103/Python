def for_Z():
        """ Upper case Alphabet letter 'Z' pattern using Python for loop"""

        for row in range(6):
                for col in range(6):
                        if row in (0,5) or row+col==5:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_Z():
        """ Upper case Alphabet letter 'Z' pattern using Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<6:
                        if row in (0,5) or row+col==5:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1


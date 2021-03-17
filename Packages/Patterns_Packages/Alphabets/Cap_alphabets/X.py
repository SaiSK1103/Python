def for_X():
        """ Upper case Alphabet letter 'X' using for loop"""

        for row in range(5):
                for col in range(6):
                        if row-col==0 or row+col==4:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_X():
        """ Upper case Alphabet letter 'X' using while loop"""

        row = 0
        while row<5:
                col = 0
                while col<6:
                        if row-col==0 or row+col==4:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

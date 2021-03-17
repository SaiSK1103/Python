def for_y():
        """ Lower case Alphabet letter 'y' pattern using Python for loop"""

        for row in range(6):
                for col in range(7):
                        if row+col==5 or row-col==0 and row<3:
                                print('*', end = '')
                        else:
                                print(' ', end = '')
                print()

def while_y():
        """ Lower case Alphabet letter 'y' pattern using Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<7:
                        if row+col==5 or row-col==0 and row<3:
                                print('*', end = '')
                        else:
                                print(' ', end = '')
                        col += 1
                print()
                row += 1


def for_V():
        """ Upper case Alphabet letter 'V' pattern using Python for loop"""

        for row in range(7):
                for col in range(13):
                        if row==col or row+col==12:
                                print('*', end = '')
                        else:
                                print(' ', end = '')
                print()


def while_V():
        """ Upper case Alphabet letter 'V' pattern using Python while loop"""

        row = 0
        while row<7:
                col = 0
                while col<13:
                        if row==col or row+col==12:
                                print('*', end = ' ')
                        else:
                                print(' ', end ='')
                        col += 1
                print()
                row += 1

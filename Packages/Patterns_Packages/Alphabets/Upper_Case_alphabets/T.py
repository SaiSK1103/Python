def for_T():
        """ Upper case Alphabet letter 'T' pattern using Python for loop"""

        for row in range(5):
                for col in range(3):
                        if row==0 or col==1:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_T():
        """ Upper case Alphabet letter 'T' pattern using Python while loop"""

        row = 0
        while row<5:
                col = 0
                while col<3:
                        if row==0 or col==1:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

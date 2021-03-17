def for_r():
        """ Lower case Alphabet letter 'r' pattern using Python for loop"""

        for row in range(5):
                for col in range(4):
                        if row==0 and col!=1 or col==1 and row>0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_r():
        """ Lower case Alphabet letter 'r' pattern using Python while loop"""

        row = 0
        while row<5:
                col = 0
                while col<4:
                        if row==0 and col!=1 or col==1 and row>0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1


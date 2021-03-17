def for_i():
        """ Lower case Alphabet letter 'i' pattern using Python for loop"""

        for row in range(6):
                for col in range(4):
                        if col==2 and row!=1 or row==5 and col>0 or col==1 and row==3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_i():
        """ Lower case Alphabet letter 'i' pattern using Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<4:
                        if col==2 and row!=1 or row==5 and col>0 or col==1 and row==3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1


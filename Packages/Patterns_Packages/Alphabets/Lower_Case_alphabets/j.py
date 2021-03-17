def for_j():
        """ Lower case Alphabet letter 'j' pattern using Python for loop"""

        for row in range(6):
                for col in range(4):
                        if col==2 and row!=1 or row==5 and col in (1,2) or col==0 and row==4 or col==1 and row==2:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_j():
        """ Lower case Alphabet letter 'j' pattern using Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<4:
                        if col==2 and row!=1 or row==5 and col in (1,2) or col==0 and row==4 or col==1 and row==2:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1


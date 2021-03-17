def for_d():
        """ Lower case Alphabet letter 'd' pattern using Python for loop"""

        for row in range(7):
                for col in range(4):
                        if col==3 or col==0 and row in (4,5) or row>0 and col>0 and row%3==0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_d():
                
        """ Lower case Alphabet letter 'd' pattern using Python while loop"""

        row = 0
        while row<7:
                col = 0
                while col<4:
                        if col==3 or col==0 and row in (4,5) or row>0 and col>0 and row%3==0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1


def for_Q():
        """ Upper case Alphabet letter 'Q' using for loop"""

        for row in range(5):
                for col in range(5):
                        if col in (0,4) and row>0 and row<4 or row in (0,4) and col>0 and col<4 or col-row==0 and row>2:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_Q():
        """ Upper case Alphabet letter 'Q' using while loop"""

        row = 0
        while row<5:
                col = 0
                while col<5:
                        if col in (0,4) and row>0 and row<4 or row in (0,4) and col>0 and col<4 or col-row==0 and row>2:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1


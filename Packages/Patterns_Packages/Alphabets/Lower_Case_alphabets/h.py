def for_h():
        """ Lower case Alphabet letter 'h' pattern using Python for loop"""

        for row in range(5):
                for col in range(4):
                        if col==0 or row==2 and col<3 or col==3 and row>2:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_h():
        """ Lower case Alphabet letter 'h' pattern using Python while loop"""

        row = 0
        while row<5:
                col = 0
                while col<4:
                        if col==0 or row==2 and col<3 or col==3 and row>2:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1


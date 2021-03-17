def for_R():
        """ Upper case Alphabet letter 'R' pattern using Python for loop"""

        for row in range(6):
                for col in range(5):
                        if col==0 or row%3==0 and col<3 or col==3 and row%3!=0 and row<3 or row-col==2:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_R():
        """ Upper case Alphabet letter 'R' pattern using Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<5:
                        if col==0 or row%3==0 and col<3 or col==3 and row%3!=0 and row<3 or row-col==2:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

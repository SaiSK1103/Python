def for_E():
        """ Upper case Alphabet letter 'E' pattern using Python for loop"""

        for row in range(7):
                for col in range(4):
                        if col==0 or row%3==0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_E():
        """ Upper case Alphabet letter 'E' pattern using Python while loop"""

        row = 0
        while row<7:
                col = 0
                while col<4:
                        if col==0 or row%3==0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row +=1

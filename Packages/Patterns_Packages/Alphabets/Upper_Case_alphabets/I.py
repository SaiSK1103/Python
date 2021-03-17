def for_I():
        """ Upper case Alphabet letter 'I' pattern using Python for loop"""

        for row in range(6):
                for col in range(5):
                        if row in (0,5) or col==2:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_I():
                
        """ Upper case Alphabet letter 'I' pattern using Python while loop"""
        row = 0
        while row<6:
                col = 0
                while col<5:
                        if row in (0,5) or col==2:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

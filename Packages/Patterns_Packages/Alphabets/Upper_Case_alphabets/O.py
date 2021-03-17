def for_O():
        """ Upper case Alphabet letter 'O' pattern using Python for loop"""

        for row in range(6):
                for col in range(5):
                        if row in (0,5) and col>0 and col<4 or col in (0,4) and row>0 and row<5:
                                print('*', end = ' ')
                        else:
                        	print(' ', end = ' ')
                print()


def while_O():
                
        """ Upper case Alphabet letter 'O' pattern using Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<5:
                        if row in (0,5) and col>0 and col<4 or col in (0,4) and row>0 and row<5:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

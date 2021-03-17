def for_J():
        """ Upper case Alphabet letter 'J' using for loop"""

        for row in range(6):
                for col in range(5):
                        if row==0 or col==2 and row<5 or row+col==6 and col<3 or col==0 and row==4:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()



def while_J():
        """ Upper case Alphabet letter 'J' using while loop"""
        row = 0
        while row<6:
                col = 0
                while col<5:
                        if row==0 or col==2 and row<5 or row+col==6 and col<3 or col==0 and row==4:
                            print('*', end = ' ')
                        else:
                            print(' ', end = ' ')
                        col += 1
                print()
                row += 1

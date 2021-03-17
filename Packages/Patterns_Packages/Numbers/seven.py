def for_seven():
        """ Number pattern '7' using Python for loop"""

        for row in range(6):
                for col in range(5):
                        if row+col==4 or row==0:
                                print('*', end = '')
                        else:
                                print(' ', end = '')
                print()


def while_seven():
                
        """ Number pattern '7' using Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<5:
                        if row+col==4 or row==0:
                                print('*', end = '')
                        else:
                                print(' ', end = '')
                        col += 1
                print()
                row += 1


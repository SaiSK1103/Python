def for_four():
        """ Number pattern '4' using Python for loop"""

        for row in range(5):
                for col in range(5):
                        if col==3 or row==3 or row+col==3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print() 

def while_four():
                
        """ Number pattern '4' using Python while loop"""

        row = 0
        while row<5:
                col = 0
                while col<5:
                        if col==3 or row==3 or row+col==3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

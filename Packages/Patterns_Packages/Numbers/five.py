def for_five():
        """ Number pattern '5' using Python for loop"""

        for row in range(7):
                for col in range(5):
                        if col==0 and row<6 and row!=4 or col>0 and col<3 and row%3==0 or col==3 and (row==0 or row>3) and row<6:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_five():
                
        """ Number pattern '5' using Python while loop"""
        row = 0
        while row<7:
                col = 0
                while col<7:
                        if col==0 and row<6 and row!=4 or col>0 and col<3 and row%3==0 or col==3 and (row==0 or row>3) and row<6:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1


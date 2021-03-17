def for_zero():
        """ Number pattern '0' using Python for loop"""

        for row in range(5):
                for col in range(5):
                        if row%4==0 and col>0 and col<4 or col%4==0 and row>0 and row<4 or row+col==4 and col!=0 and row!=0:
                                print('*', end = '')
                        else:
                                print(' ', end = '')
                print()

def while_zero():
                
        """ Number pattern '0' using Python while loop"""

        row = 0
        while row<5:
                col = 0
                while col<5:
                        if row%4==0 and col>0 and col<4 or col%4==0 and row>0 and row<4 or row+col==4 and col!=0 and row!=0:
                                print('*', end = '')
                        else:
                                print(' ', end = '')
                        col += 1
                print()
                row += 1


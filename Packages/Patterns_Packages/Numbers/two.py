def for_two():
        """ Number pattern '2' using Python for loop"""

        for row in range(5):
                for col in range(4):
                        if row==0 and col>0 and col<3 or col==0 and row==1 or row+col==4 or row==4:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_two():
        """ Number pattern '2' using Python while loop"""

        row = 0
        while row<5:
                col = 0
                while col<4:
                        if row==0 and col>0 and col<3 or col==0 and row==1 or row+col==4 or row==4:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1


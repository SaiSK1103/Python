def for_eight():
        """ Number pattern '8' using Python for loop"""

        for row in range(7):
                for col in range(5):
                        if row%3==0 and col>0 and col<4 or col%4==0 and row%3!=0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_eight():
        """ Number pattern '8' using Python while loop"""

        row = 0
        while row<7:
                col = 0
                while col<5:
                        if row%3==0 and col>0 and col<4 or col%4==0 and row%3!=0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

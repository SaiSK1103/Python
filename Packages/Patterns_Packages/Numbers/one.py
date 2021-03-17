def for_one():
        """ Number pattern '1' using Python for loop"""

        for row in range(6):
                for col in range(3):
                        if col==1 or row==5 or col==0 and row==1:
                                print('1', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_one():
                

        """ Number pattern '1' using Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<3:
                        if col==1 or row==5 or col==0 and row==1:
                                print('1', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1


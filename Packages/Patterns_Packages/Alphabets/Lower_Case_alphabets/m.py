def for_m():
        """ Lower case Alphabet letter 'n' pattern using Python for loop"""

        for row in range(4):
                for col in range(5):
                        if row==0 and (col==0 or col%2!=0) or row>0 and col%2==0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_m():
        """ Lower case Alphabet letter 'm' pattern using Python while loop"""

        row = 0
        while row<4:
                col = 0
                while col<5:
                        if row==0 and (col==0 or col%2!=0) or row>0 and col%2==0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1


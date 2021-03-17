def for_z():
        """ Lower case Alphabet letter 'z' pattern using Python for loop"""

        for row in range(4):
                for col in range(4):
                        if row==0 or row==3 or row+col==3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print() 

def while_z():
        """ Lower case Alphabet letter 'z' pattern using Python while loop"""

        row = 0
        while row<4:
                col = 0
                while col<4:
                        if row==0 or row==3 or row+col==3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1


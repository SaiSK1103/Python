def for_x():
        """ Lower case Alphabet letter 'x' pattern using Python for loop"""

        for row in range(5):
                for col in range(5):
                        if row-col==0 or row+col==4:
                                print('*', end = '')
                        else:
                                print(' ', end = '')
                print()

def while_x():
        """ Lower case Alphabet letter 'x' pattern using Python while loop"""

        row = 0
        while row<5:
                col = 0
                while col<5:
                        if row-col==0 or row+col==4:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1


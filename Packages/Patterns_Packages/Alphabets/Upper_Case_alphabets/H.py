def for_H():
        """ Upper case Alphabet letter 'H' pattern using Python for loop"""

        for row in range(7):
                for col in range(5):
                        if col%4==0 or row==3:
                                print('*', end =' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_H():
        """ Upper case Alphabet letter 'H' pattern using Python while loop"""
        row = 0
        while row<7:
                col = 0
                while col<5:
                        if col%4==0 or row==3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

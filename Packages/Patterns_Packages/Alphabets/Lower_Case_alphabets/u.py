def for_u():
        """ Lower case Alphabet letter 'u' pattern using Python for loop"""

        for row in range(4):
                for col in range(4):
                        if col%3==0 and row<3 or row==3 and col>0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_u():
        """ Lower case Alphabet letter 'u' pattern using Python while loop"""

        row = 0
        while row<4:
                col = 0
                while col<4:
                        if col%3==0 and row<3 or row==3 and col>0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1


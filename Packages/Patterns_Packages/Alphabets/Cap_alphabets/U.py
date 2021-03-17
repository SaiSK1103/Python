def for_U():
        """ Upper case Alphabet letter 'U' using for loop"""

        for row in range(6):
                for col in range(5):
                        if col%4==0 and row<5 or row==5 and col>0 and col<4:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()
                

def while_U():
        """ Upper case Alphabet letter 'U'"""

        row = 0
        while row<6:
                col = 0
                while col<5:
                        if col%4==0 and row<5 or row==5 and col>0 and col<4:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1



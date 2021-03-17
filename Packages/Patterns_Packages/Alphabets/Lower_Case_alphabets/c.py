def for_c():
        """ Lower case Alphabet letter 'c' pattern using Python for loop"""

        for row in range(4):
                for col in range(4):
                        if col==0 and row%3!=0 or col>0 and row%3==0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_c():
                
        """ Lower case Alphabet letter 'c' patter using Python while loop"""

        row = 0
        while row<4:
                col = 0
                while col<4:
                        if col==0 and row%3!=0 or col>0 and row%3==0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1


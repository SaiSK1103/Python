def for_o():
        """ Lower case Alphabet letter 'o' pattern using Python for loop"""

        for row in range(4):
                for col in range(4):
                        if row%3==0 and col in (1,2) or col%3==0 and row in (1,2):
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')	
                print()


def while_o():
        """ Lower case Alphabet letter 'o' pattern using Python while loop"""

        row = 0
        while row<4:
                col = 0
                while col<4:
                        if row%3==0 and col in (1,2) or col%3==0 and row in (1,2):
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1


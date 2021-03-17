def for_b():
        """ Lower case Alphabet letter 'b' pattern using Python for loop"""

        for row in range(7):
                for col in range(4):
                        if col==0 or row!=0 and row%3==0 and col<3 or col==3 and row in (4,5):
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_b():
                
        """ Lower case Alphabet letter 'b' pattern using Python while loop"""

        row = 0
        while row<7:
                col = 0
                while col<4:
                        if col==0 or row!=0 and row%3==0 and col<3 or col==3 and row in (4,5):
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1


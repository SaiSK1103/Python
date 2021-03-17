def for_q():
        """ Lower case Alphabet letter 'q' pattern using Python for loop"""

        for row in range(6):
                for col in range(4):
                        if col>0 and col<2 and row%3==0 or col==0 and row in (1,2) or col==2 or col==3 and row==4:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print() 

def while_q():
        """ Lower case Alphabet letter 'q' pattern using Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<4:
                        if col>0 and col<2 and row%3==0 or col==0 and row in (1,2) or col==2 or col==3 and row==4:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1


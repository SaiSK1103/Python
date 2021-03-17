def for_G():
        """ Upper case Alphabet letter 'G' pattern using Python for loop"""

        for row in range(7):
                for col in range(5):
                        if col==0 and row>0 and row<6 or row%3==0 and col>0 and col<4 and row!=3 or row==3 and col>1 or col==4 and (row>2 and row<6 or row==1):
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()
def while_G():
        """ Upper case Alphabet letter 'G' pattern using Python while loop"""

        row = 0
        while row<7:
                col = 0
                while col<5:
                        if col==0 and row>0 and row<6 or row%3==0 and col>0 and col<4 and row!=3 or row==3 and col>1 or col==4 and (row>2 and row<6 or row==1):
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row +=1

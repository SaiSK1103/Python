def for_W():
        """ Upper case Alphabet letter 'W' pattern using Python for loop"""

        for i in range(5):
                for j in range(27):
                        if (i==j or (i>1 and (i+j==8) or (i+j==13)) or (i==3 and i+j==11)):
                                print('*', end = '')
                        else:
                                print(' ', end = '')
                print()


def while_W():
        """ Upper case Alphabet letter 'W' pattern using Python while loop"""

        row = 0
        while row<5:
                col = 0
                while col<27:
                        if row==col or row>1 and row+col==8 or row+col==13 or row==3 and row+col==11:
                                print('*', end = '')
                        else:
                                print(' ', end = '')
                        col +=1
                print()
                row += 1


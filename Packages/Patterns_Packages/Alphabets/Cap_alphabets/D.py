# using for loop

def for_D():
        """ Upper case Alphabet letter 'D' pattern using for loop"""

        for row in range(6):
                for col in range(5):
                        if col==0 or row in (0,5) and col<4 or col==4 and row>0 and row<5:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

# using while loop
def while_D():
        """ Upper case Alphabet letter 'D' pattern using while loop"""

        row = 0
        while row<6:
                col = 0
                while col<5:
                        if col==0 or row in (0,5) and col<4 or col==4 and row>0 and row<5:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col +=1
                print()
                row +=1


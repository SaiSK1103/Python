def for_C():
        """ Upper case Alphabet letter 'C' pattern using Python for loop"""

        for row in range(6):
                for col in range(5):
                        if row in (0,5) and col>0 and col<4 or col==0 and row>0 and row<5 or col==4 and row in (1,4):
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_C():
        """ Upper case Alphabet letter 'C' pattern using Python while loop"""
        row = 0
        while row<6:
                col = 0
                while col<5:
                        if row in (0,5) and col>0 and col<4 or col==0 and row>0 and row<5 or col==4 and row in (1,4):
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row +=1

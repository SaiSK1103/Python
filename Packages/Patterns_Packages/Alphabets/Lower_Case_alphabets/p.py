def for_p():
        """ Lower case Alphabet letter 'p' pattern using Python for loop"""

        for row in range(5):
                for col in range(4):
                        if col==0 or row%2==0 and row!=4 and col<3 or col==3 and row==1:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_p():
        """ Lower case Alphabet letter 'p' pattern using Python while loop"""

        row = 0
        while row<5:
                col = 0
                while col<4:
                        if col==0 or row%2==0 and row!=4 and col<3 or col==3 and row==1:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1


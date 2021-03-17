def for_s():
        """ Lower case Alphabet letter 's' pattern using Python for loop"""

        for row in range(7):
                for col in range(5):
                        if row%3==0 and col>0 and col<4 or col==0 and row%3!=0 and row!=4 or col==4 and row%3!=0 and row!=2:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_s():
        """ Lower case Alphabet letter 's' pattern using Python while loop"""

        row = 0
        while row<7:
                col = 0
                while col<5:
                        if row%3==0 and col>0 and col<4 or col==0 and row%3!=0 and row!=4 or col==4 and row%3!=0 and row!=2:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1


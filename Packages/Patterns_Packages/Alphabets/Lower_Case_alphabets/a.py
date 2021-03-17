def for_a():
        """ Lower case Alphabet letter 'a' pattern using Python for loop """


        for row in range(7):
                for col in range(5):
                        if row%3==0 and col>0 and col<4 or col==0 and row in (1,4,5) or col==4 and row>0 :
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_a():
                
        """ Small case Alphabet letter 'a' pattern using Python while loop"""

        row = 0
        while row<7:
                col = 0
                while col<5:
                        if row%3==0 and col>0 and col<4 or col==0 and row in (1,4,5) or col==4 and row>0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1


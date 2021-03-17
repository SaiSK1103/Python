def for_P():
        """ Upper case Alphabet letter 'P' using for loop"""

        for row in range(6):
                for col in range(4):
                        if col==0 or row%3==0 and col<3 or col==3 and row%3!=0 and row<3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')

                print()

def while_P():
                
        """ Upper case Alphabet letter 'P' using while loop"""

        row = 0
        while row<6:
                col = 0
                while col<4:
                        if col==0 or row%3==0 and col<3 or col==3 and row%3!=0 and row<3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row +=1


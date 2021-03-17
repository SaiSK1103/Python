def for_rectangle():
        """Shape of 'Rectangle' using Python for loop """

        for row in range(6):
                for col in range(8):
                        if row==0 or col==0 or row==5 or col==7:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()
                
def while_rectangle():
        """Shape of 'Rectangle' using Python while loop """
        row = 0
        while row<6:
                col = 0
                while col<8:
                
                        if row==0 or col==0 or row==5 or col==7:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1
                
                

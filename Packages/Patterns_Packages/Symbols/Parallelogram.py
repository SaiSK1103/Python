def for_parallelogram():
        """Shape of 'Parallelogram' using Python for loop """

        for row in range(6):
                print(' '*(5-row), end = ' ')
                for col in range(9):
                        if row==0 or col==0 or row==5 or col==8:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_parallelogram():
        """Shape of 'Parallelogram' using Python while loop """
        row = 0
        while row<6:
                print(' '*(5-row), end = ' ')
                col = 0
                while col<9:
                        if row==0 or col==0 or row==5 or col==8:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        
                        col +=1
                print()
                row += 1
                            

def for_rhombus():
        """Shape of 'Rhombus' using Python for loop """
        
        for row in range(9):
                for col in range(9):
                        if row+col==4 or col-row==4 or row-col==4 or row+col==12:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_rhombus():
        """Shape of 'Rhombus' using Python while loop """
        row = 0
        while row<9:
                col = 0
                while col<9:
                        if row+col==4 or col-row==4 or row-col==4 or row+col==12:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

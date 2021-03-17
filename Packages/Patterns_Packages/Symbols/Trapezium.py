def for_trapezium():
        """Shape of 'Trapezium' using Python for loop """

        for row in range(6):
                print(' '*(5-row), end = ' ')
                for col in range(14):
                        if row==0 and col<9 or col==0 or row==5 or col-row==8:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_trapezium():
        """Shape of 'Trapezium' using Python while loop """

        row = 0
        while row<6:

                print(' '*(5-row), end = ' ')
                col = 0
                while col<14:
                        if row==0 and col<9 or col==0 or row==5 or col-row==8:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

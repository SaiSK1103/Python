def for_square():
        """Shape of 'Square' using Python for loop """

        for row in range(5):
                for col in range(5):
                        if row==0 or col==0 or row==4 or col==4:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_square():
        """Shape of 'Square' using Python while loop """

        row = 0
        while row<5:
                col = 0
                while col<5:
                        if row==0 or col==0 or row==4 or col==4:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

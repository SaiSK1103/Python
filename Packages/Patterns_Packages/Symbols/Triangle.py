def for_triangle():
        """Shape of 'Triangle' using Python for loop"""

        for row in range(6):
                for col in range(6):
                        if row<=col:
                                print(' ', end = ' ')
                        else:
                                print('*', end = ' ')
                print()

def while_triangle():
        """Shape of 'Triangle' using Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<6:
                        if row<=col:
                                print(' ', end = ' ')
                        else:
                                print('*', end = ' ')

                        col += 1
                print()
                row += 1

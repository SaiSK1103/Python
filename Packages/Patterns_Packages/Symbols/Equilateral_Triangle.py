
def for_equilateral_triangle():
        """Shape of 'Equilateral Triangle' using Python for loop"""

        for row in range(12):
                if row%2!=0:
                        print(' '*(12-row), '* '*row)
def while_equilateral_triangle():
        """Shape of 'Equilateral Triangle' using Python while loop"""
        row = 0
        while row<12:
                if row%2!=0:
                        print(' '*(12-row), '* '*row)
                row += 1


def for_isosceles_triangle():
        """Shape of 'Isosceles Triangle' using Python for loop"""

        for row in range(7):
                print(' '*(7-row), '* '*row)

def while_isosceles_triangle():
        """Shape of 'Isosceles Triangle' using Python while loop """
        row = 0
        while row<7:
                print(' '*(7-row), '* '*row)
                row += 1

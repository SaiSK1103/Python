def for_kite():
        """Pattern of 'Kite' using Python for loop """

        for row in range(9):
                if row%2!=0:
                        print(' '*(10-row), '* '*row)
        for col in range(10):
                print(' '*(col+1),'* '*(9-col))
                
def while_kite():
        """Pattern of 'Kite' using Python while loop """

        row = 0
        while row<9:
                if row%2!=0:
                        print(' '*(10-row), '* '*row)
                row += 1
        col = 0
        while col<10:
                print(' '*(col+1),'* '*(9-col))
                col += 1
                

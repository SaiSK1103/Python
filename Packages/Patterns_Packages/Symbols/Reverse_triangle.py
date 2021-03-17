def for_reverse_triange():
        """Shape of 'Reverse Triangle' using Python for loop """

        for row in range(6,0,-1):
                print(' '*(6-row), '* '*row)
                

def while_reverse_triange():
        """Shape of 'Reverse Triangle' using Python while loop """
        row = 6
        while row>0:
                
                print(' '*(6-row), '* '*row)
                row -= 1
                


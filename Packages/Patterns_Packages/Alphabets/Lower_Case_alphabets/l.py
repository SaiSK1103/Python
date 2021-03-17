def for_l():
        """ Lower case Alphabet letter 'l' pattern using Python  for loop"""

        for row in range(6):
                for col in range(3):
                        if col==0 and row==5 or col==1 and row!=5 or col==2 and row==5:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print() 

def while_l():
                
        """ Lower case Alphabet letter 'l' pattern using Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<3:
                        if col==0 and row==5 or col==1 and row!=5 or col==2 and row==5:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1


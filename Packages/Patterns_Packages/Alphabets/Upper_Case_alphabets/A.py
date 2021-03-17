def for_A():
        """ Upper case Alphabet letter 'A' pattern using Python for loop"""
        for row in range(6):
                for col in range(5):
                        if row==0 and col%4!=0 or col%4==0 and row>0 or row==3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_A():
        """ Upper case Alphabet letter 'A' pattern using Python while loop"""
        row = 0
        while row<6:
                col = 0
                while col<5:
                        if row==0 and col%4!=0 or col%4==0 and row>0 or row==3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1
                

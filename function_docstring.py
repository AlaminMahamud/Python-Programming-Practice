__author__ = 'Root'
def print_max(x,y):
    '''Prints the Maximum of two numbers
    The Two Values must be integers'''
    #convert to integers, if possible
    x = int(x)
    y = int(y)

    if x>y:
        print(x, ' is maximum')
    else:
        print(y, ' is maximum')
print_max(3,5)
print(print_max.__doc__)
__author__ = 'Root'
def print_max(a,b):
    if(a>b) :
        print("{} is greater than {}".format(a,b))
    elif(a<b):
        print("{} is greater than {}".format(b,a))
    else:
        print("they are equal")
print_max(3,4)
print_max(4,3)
print_max(4,4)
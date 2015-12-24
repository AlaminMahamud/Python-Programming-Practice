__author__ = 'Root'
def func(a,b=10,c=20):
    print('a is ',a,' b is ', b, ' c is ',c)
func(5)
func(5,15,25)
func(a=5)
func(c=21,b=25,a=100)

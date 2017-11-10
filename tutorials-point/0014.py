#!/usr/bin/python3
a = 10
b = 20
list = [1,2,3,4,5,6,7,8,9,10]

if(a in list):
    print('a is in list')
    print('This is line 2')
else:
    print('a is not in list')
    
if(b not in list):
    print('b is not in list')
else:
    print('b is in list')
    
a = 2
if( a in list ):
    print("Line 3 - a is available in the given list")
else:
    print("Line 3 - a is not available in the given list")

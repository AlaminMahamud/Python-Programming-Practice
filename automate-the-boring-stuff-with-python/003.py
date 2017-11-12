#comma code
list = ['alamin', 'anika', 'anamika']
len = len(list)
str = ''
for i in range(len):
    if(i==len-1):
        str += 'and ' + list[i]
    else:
        str += list[i] + ', '
print str

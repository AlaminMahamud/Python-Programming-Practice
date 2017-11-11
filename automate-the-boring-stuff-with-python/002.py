def collatz(num):
    if(num == 1):
        return
    elif(num%2 == 0):
        print(num/2)
        collatz(num/2)
    else:
        print(num*3+1)
        collatz(num*3+1)
while True:
    num = input('please input a number\n')
    try:
        x = int(num)
        collatz(x)
    except:
        print('OOps! That was no valid number. Try again...')
        
    
    

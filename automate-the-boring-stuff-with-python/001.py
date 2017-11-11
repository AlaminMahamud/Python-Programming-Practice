import sys

def collatz(num):
    if(num == 1):
        return
    elif(num % 2 == 0):
        print(num / 2)
        return collatz (num / 2)
    else:
        print((3 * num + 1))
        return collatz(3 * num + 1)

while True:
    num = int(input('input number\n'))
    collatz(num)

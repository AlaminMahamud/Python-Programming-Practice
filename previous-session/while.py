__author__ = 'Root'
number = 23
running = True
guess = int(input("Enter a number : \n"))
while running:
    if guess == number:
        print('Congrats you gets it')
    elif guess<=number:
        print("Number is Little Higher")
    else:
        print("Number is Little Lower")
    print("Always will execute")
    if 0 == guess:
        running = False
    guess-=1
print('After While')
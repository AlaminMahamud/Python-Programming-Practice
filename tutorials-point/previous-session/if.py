__author__ = 'Root'
number = 23
guess = int(input('Enter an Integer : '))

if guess == number:
    #New Block starts Here
    print('Congratulations you guessed it')
    print('but you donot win any prizes')
    #New Block ends Here
elif guess>number:
    #another Block
    print('Guess is Gettter than Number')
    #end another Block
else:
    #Last Block
    print('No it is little lower than that')
    #End Of Last Block

#The Last Statement is always executed
#After the if statement is executed
print('Done')

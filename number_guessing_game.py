from random import randint


def random_number(number, holder):
    holder3 = holder
    if number == holder3:
        print('you got the right number!')
    elif number > holder3:
        number = int(input('the number you entered is too high, choose a new number! \n'))
        random_number(number, holder3)
    elif number < holder3:
        number = int(input('the number you entered is too low, choose a new number! \n'))
        random_number(number, holder3)


x, y, z = input('welcome to my random number generator. choose a base number: ').split(',')
print('enter the first number: ', x)
print('enter the second number: ', y)
print('Now enter a random number between your two values:', z)
holder1 = randint(int(x), int(y))


# number1 = int(input('welcome to my random number generator. go ahead and type in a number between 0 - 20 \n'))


random_number(int(z), holder1)

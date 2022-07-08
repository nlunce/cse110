import math
import random



def guess_loop():
    magic_number = random.randint(0,100)
    print('The magic number is between 0 and 100!')
    guess = float(input('What is your guess?: '))

    guess_counter = 0
    while guess != magic_number:
        guess_counter += 1
        print(f'GUESS COUNTER: {guess_counter}')
        if guess > magic_number:
            print('Lower')
            guess = float(input('What is your guess?: '))
        elif guess < magic_number:
            print('Higher')
            guess = float(input('What is your guess?: '))


guess_loop()


print('You guessed it!')
play_again = input('Do you want to play again?(yes/no): ')

if play_again.lower() == 'yes':
    guess_loop()
else:
    print('Thanks for playing!')

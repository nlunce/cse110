from itertools import count
import random
import math

def main():
    word_picker_function()
    guess_counter = 0
    print('Welcome to the word guessing game!')
    print('Your hint is: ' + ''.join(list_hint))
    guess = input('What is your guess?: ').lower()
    guess_counter += 1
    global list_guess
    list_guess = list(guess)
    

    if len(list_guess) > len(list_secret_word):
        appender()


    while (''.join(list_secret_word[0:default_secret_word_length])) != ''.join(list_guess[0:default_secret_word_length]):
        hint_maker()
        print('Your hint is: ' + ''.join(list_hint))
        guess = input('What is your guess?: ').lower()
        list_guess = list(guess)
        guess_counter += 1
        if len(list_guess) > len(list_secret_word):
            appender()

    play_again = input(f'Congratulations! You guessed it!\nIt took you {guess_counter} guesses.\nWould you like to play again? (yes/no): ')
    if play_again.lower() == 'yes':
        main()
    else:
        print('Thank you for playing!')

def word_picker_function():
    secret_word_list = ['fortnite', 'cheese', 'dinosaur', 'chicken', 'pickle', 'computer', 'rainbow', 'remember', 'desktop', 'finger', 'alien']
    word_picker = random.randint(0,10)
    secret_word = secret_word_list[word_picker]
    global list_hint
    global list_secret_word
    global default_secret_word_length
    list_hint = ['_' for q in range(len(secret_word))]
    list_secret_word = list(secret_word)
    default_secret_word_length = len(list_hint)

def appender():
    length_of_guess = len(list_guess)
    add_amount = length_of_guess - len(list_secret_word)
    add_amount_range = range(add_amount)
    for i in add_amount_range:
        list_secret_word.append(' ')
        list_hint.append('_')

def hint_maker():
    count = 0
    for letter in list_guess:
        if letter == list_secret_word[count]:
            list_hint[count] = letter.capitalize()
            count += 1
        elif letter in list_secret_word:
            list_hint[count] = letter.lower()
            count += 1
        else:
            count +=1

main()


        




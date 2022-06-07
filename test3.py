import random
import math

def main():
    word_picker_function()
    global guess
    list_hint = ['_' for q in range(len(secret_word))]
    string_hint = (''.join(list_hint))
    guess_counter = 0
    
    print('Welcome to the word guessing game!')
    print(f'Your hint is: {string_hint}')
    guess = input('What is your guess?: ')
    guess_counter += 1

   

    while guess != secret_word:
        print('Your guess was not correct.')
        
        if len(guess) > len(secret_word):
            interim_secret_word_function()
            interim_hint = ['_' for i in range(len(guess))]
            for i, letter in enumerate(guess):
                if letter == interim_secret_word[i]:
                    interim_hint[i] = letter.upper()
                elif letter in interim_secret_word:
                    interim_hint[i] = letter.lower()
            interim_string_hint = (''.join(interim_hint))
            print(f'Your hint is {interim_string_hint}')
            guess = input('What is your guess?: ')
            guess_counter += 1

        else:
            list_hint = ['_' for i in range(len(secret_word))]
            for i, letter in enumerate(guess):
                if letter == secret_word[i]:
                    list_hint[i] = letter.upper()
                elif letter in secret_word:
                    list_hint[i] = letter.lower()
            string_hint = (''.join(list_hint))
                
            print(f'Your hint is {string_hint}')
            guess = input('What is your guess?: ')
            guess_counter += 1

    play_again = input(f'Congratulations! You guessed it!\nIt took you {guess_counter} guesses.\nWould you like to play again? (yes/no): ')
    if play_again.lower() == 'yes':
        main()
    else:
        print('Thank you for playing!')



def word_picker_function():
    global secret_word
    secret_word_list = ['fortnite', 'cheese', 'dinosaur', 'chicken', 'pickle', 'computer', 'rainbow', 'remember', 'desktop', 'finger', 'alien']
    word_picker = random.randint(0,10)
    secret_word = secret_word_list[word_picker]

def interim_secret_word_function():
    global interim_secret_word
    list_interim_secret_word = list(secret_word)
    add_amount = len(guess) - len(secret_word)
    range_add = range(add_amount)
    for i in range_add:
        list_interim_secret_word.append('_')
    interim_secret_word = (''.join(list_interim_secret_word))

    
main()
import random
import math





def word_picker_function():
    secret_word_list = ['fortnite', 'cheese', 'dinosaur', 'chicken', 'pickle', 'computer', 'rainbow', 'remember', 'desktop', 'finger', 'alien']
    word_picker = random.randint(0,10)
    secret_word = secret_word_list[word_picker]
    global list_hint
    global list_secret_word
    list_hint = ['_' for q in range(len(secret_word))]
    list_secret_word = list(secret_word)


def game():
    count = 0
    global list_guess
    global guess

    if len(list_guess) > len(list_secret_word):
        length_of_guess = len(list_guess)
        add_amount = length_of_guess - len(list_secret_word)
        add_amount_range = range(add_amount)
        for i in add_amount_range:
            list_secret_word.append('_')
            list_hint.append('_')



    while list_guess != list_secret_word:
        for letter in list_guess:
            if letter == list_secret_word[count]:
                list_hint[count] = letter.capitalize()
                count += 1
            elif letter in list_secret_word:
                list_hint[count] = letter.lower()
                count += 1
            else:
                count +=1
        print('Your hint is: ' + ''.join(list_hint))
        guess = input('What is your guess?: ').lower()
        list_guess = list(guess)




word_picker_function()

print('Welcome to the word guessing game!')

print('Your hint is: ' + ''.join(list_hint))
guess = input('What is your guess?: ').lower()
list_guess = list(guess)


game()
    














# print('Your hint is: ' + ''.join(list_hint))
# guess = input('What is your guess?: ').lower()
# list_guess = list(guess)
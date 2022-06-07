import random
import math

def main():
    word_picker_function()
    list_hint = ['_' for q in range(len(secret_word))]
    string_hint = (''.join(list_hint))
    
    print('Welcome to the word guessing game!')
    print(f'Your hint is: {string_hint}')
    guess = input('What is your guess?: ')

   

    while guess != secret_word:
        list_hint = ['_' for q in range(len(secret_word))]
        for i, letter in enumerate(guess):
            for j in enumerate(secret_word):
                if letter == secret_word[i]:
                    





        string_hint = (''.join(list_hint))
            
        print(f'Your hint is {string_hint}')
        guess = input('What is your guess?: ')




    



def word_picker_function():
    global secret_word
    secret_word_list = ['fortnite', 'cheese', 'dinosaur', 'chicken', 'pickle', 'computer', 'rainbow', 'remember', 'desktop', 'finger', 'alien']
    word_picker = random.randint(0,10)
    secret_word = secret_word_list[word_picker]
    
    
    
    

    

main()
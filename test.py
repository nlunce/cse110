secret_word = 'fortnite'
hint = '________'
list_hint = list(hint)
list_secret_word = list(secret_word)

print('Welcome to the word guessing game!')



 


print(f'Your hint is: {hint}')
guess = input('What is your guess?: ').lower()
list_guess = list(guess)
count = 0

if len(list_guess) > len(list_secret_word):
    length_of_guess = len(list_guess)
    add_amount = length_of_guess - len(list_secret_word)
    add_amount_range = range(add_amount)
    for i in add_amount_range:
        list_hint.append('_')

print(list_hint)





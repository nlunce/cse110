secret_word = 'fortnite'
hint = '________'
list_hint = list(hint)
list_secret_word = list(secret_word)
count = 0


print('Welcome to the word guessing game!')
 

print(f'Your hint is: {hint}')
guess = input('What is your guess?: ').lower()
list_guess = list(guess)

if len(list_guess) > len(list_secret_word):
    length_of_guess = len(list_guess)
    add_amount = length_of_guess - len(list_secret_word)
    add_amount_range = range(add_amount)
    for i in add_amount_range:
        list_secret_word.append('_')
        list_hint.append('_')


    


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


    
        


                
                
            
                    
                    


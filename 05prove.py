from ast import If
import math

decision1 = input('Rowley from the popular book series "Diary of a Wimpy Kid" wakes you up. You are in a dark McDonalds, it is 3:00 in the morning. \nRowley asks you if we should STAY in the McDonalds or LEAVE?\nSTAY or LEAVE: ')

while decision1.lower() != 'leave' and decision1.lower() != 'stay':
    decision1 = input('INVALID INPUT\nLEAVE or STAY: ')
        



if decision1.lower() == 'leave':
    decision2 = input('You and Rowley leave the McDonalds, its dark, you see a large homeless man with a baseball bat.\nThe homeless man starts yelling incoherent statements about the Vietnam War and begins to run toward you.\nDo you FIGHT or RUN?\nFIGHT or RUN: ')
    
    while decision2.lower() != 'fight' and decision2.lower() != 'run':
        decision2 = input('IMPROPER INPUT\nFIGHT or RUN: ')
        
elif decision1.lower() == 'stay':
    decision2 = input('You and Rowley stay in the McDonalds till morning. A homeless man knocks on the door to the McDonalds.\nDo you OPEN the door for him or REFUSE to let him in?\nOPEN or REFUSE: ')
       
    while decision2.lower() != 'open' and decision2.lower() != 'refuse':
        decision2 = input('IMPROPER INPUT\nOPEN or REFUSE: ')

      


    
if decision2.lower() == 'fight':
    decision3 = input('You underestimated the homeless man and as he gets closer you realize he is a huge brute of a man. You are weaponless where as he has a baseball bat.\nThe homeless man beats you and Rowley up and leaves.\nDo you SHOUT for help or tell Rowley to CALL an ambulance?\nSHOUT or CALL: ')

    while decision3.lower() != 'shout' and decision2.lower() != 'call':
        decision3 = input('IMPROPER INPUT\nSHOUT or CALL: ')

elif decision2.lower() == 'run':
    decision3 = input('You and Rowley run and make it to safety. Rowley asks you if you want to have a TICKLE FIGHT or NOT.\nTICKLE FIGHT or NOT: ')

    while decision3.lower() != 'tickle fight' and decision2.lower() != 'not':
        decision3 = input('IMPROPER INPUT\nTICKLE FIGHT or NOT: ')

elif decision2.lower() == 'open':
    decision3 = input('You open the door for the homeless man and he is greatful for you compassion on him. He enlightens you with stories of the Vietnam war.\nThe homeless man offers you drugs. Do you TAKE or DENY them?\nTAKE or DENY: ')

    while decision3.lower() != 'take' and decision2.lower() != 'deny':
        decision3 = input('IMPROPER INPUT\nTAKE or DENY: ')

elif decision2.lower() == 'refuse':
    decision3 = input('You refuse to open the door for the homeless man and he becomes agressive. He pulls out a baseball bat and breakes down the door. Do you HIDE or try to TALK to him?\nHIDE or TALk: ')

    while decision3.lower() != 'hide' and decision2.lower() != 'talk':
        decision3 = input('IMPROPER INPUT\nHIDE or TALK: ')




if decision3.lower() == 'shout':
    print('You shout for help but the only one who hears is the homeless man who is half way down the block. He decides to come back and finish you and Rowley off.\nGAME OVER')
elif decision3.lower() == 'call':
    print('Rowley calls 911 and a ambulance comes and takes you to a hospital. You and Rowley make full recoveries and live happily ever after!\nGAME OVER')
elif decision3.lower() == 'tickle fight':
    print('You and Rowley have an epic tickle fight and live happily ever after!\nGAME OVER')
elif decision3.lower() == 'not':
    print('Rowley takes offense that you don\'t want to have a tickle fight. He gets angry and beats you to death.\nGAME OVER')
elif decision3.lower() == 'take':
    print('You take the homeless man\'s drugs and you instantly die from an overdose. DON\'T DO DRUGS!\nGAME OVER')
elif decision3.lower() == 'deny':
    print('You deny the drugs and the homeless man is proud of you. He says it was only a test. The three of you have a tickle fight and live happily ever after!\nGAME OVER')
elif decision3.lower() == 'hide':
    print('You and Rowley hide but the homeless man finds you. He beats you to death with a baseball bat!\nGAME OVER')
elif decision3.lower() == 'talk':
    print('You talk to the homeless man and he tells you that he is just lonely and looking for friends. You and Rowley become his friends and have a tickle fight. You live happily ever after!\nGAME OVER')
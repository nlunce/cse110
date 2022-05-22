from ast import If
import math

decision1 = input('Rowley from the popular book series "Diary of a Wimpy Kid" wakes you up. You are in a dark McDonalds, it is 3:00 in the morning. \nRowley asks you if we should STAY in the McDonalds or LEAVE?\nSTAY or LEAVE: ')

if decision1.lower() != 'leave' or decision1.lower() != 'stay':
    decision1 = input('INVALID INPUT\nLEAVE or STAY: ')
        

if decision1.lower() == 'leave':
    decision2 = input('You and Rowley leave the McDonalds, its dark, you see a large homeless man with a baseball bat.\nThe homeless man starts yelling incoherent statements about the Vietnam War and begins to run toward you.\nDo you FIGHT or RUN?\nFIGHT or RUN: ')
    
    while decision2.lower() != 'fight' or decision2.lower() != 'run':
        decision2 = input('IMPROPER INPUT\nFIGHT or RUN: ')
        if decision2.lower() == 'fight' or decision2.lower() == 'run':
            break

elif decision1.lower() == 'stay':
    decision2 = input('You and Rowley stay in the McDonalds till morning. A homeless man knocks on the door to the McDonalds.\nDo you OPEN the door for him or REFUSE to let him in?\nOPEN or REFUSE: ')
       
    while decision2.lower() != 'open' or decision2.lower() != 'refuse':
        decision2 = input('IMPROPER INPUT\nOPEN or REFUSE: ')
        if decision2.lower() == 'open' or decision2.lower() == 'refuse':
            break

    
    
if decision2.lower() == 'fight':
    print('You underestimated the homeless man and as he gets closer you realize he is a huge brute of a man. You are weaponless where as he has a baseball bat.\nThe homeless man beats you to death.\nGAME OVER')
elif decision2.lower() == 'run':
    print('You and Rowley run and make it to safety. You and Rowley have a tickle fight and you live happily ever after.\nGAME OVER')
elif decision2.lower() == 'open':
    print('You open the door for the homeless man and he is greatful for you compassion on him. He enlightens you with stories of the Vietnam war.\nThe three of you proceed to have a tickle fight and live happily ever after.\nGAME OVER')
elif decision2.lower() == 'refuse':
    print('You refuse to open the door for the homeless man and he becomes agressive. He pulls out a baseball bat and breakes down the door and the and proceeds to beat you to death.\nGAME OVER')
import math


age_one = int(input('What is the age of the first rider?: '))
height_one = int(input('What is the height of the first rider in inches?: '))
second_rider = input('Is there a second rider (yes/no)?: ')

if second_rider == 'yes':
    age_two = int(input('What is the age of the second rider?: '))
    height_two = int(input('What is the height of the second rider in inches?: '))
    if age_two >= 18 or age_one >= 18:
        if height_one >= 36 and height_two >= 36:
            print('Welcome to the ride. Please be safe and have fun!')
else:
    print('Sorry, you may not ride.')



if age_one >= 18 and height_one >= 62:
    print('Welcome to the ride. Please be safe and have fun!')
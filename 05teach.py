import math

grade_in = float(input('What is your letter (0-100)?: '))
letter = 'A'
if grade_in >= 97:
    letter = 'A'
elif grade_in < 97 and grade_in >= 93:
    letter = 'A'
elif grade_in < 93 and grade_in >= 90:
    letter = 'A-'
elif grade_in < 90 and grade_in >= 87:
    letter = 'B+'
elif grade_in < 87 and grade_in >= 83:
    letter = 'B'
elif grade_in < 83 and grade_in >= 80:
    letter = 'B-'
elif grade_in < 80 and grade_in >= 77:
    letter = 'C+'
elif grade_in < 77 and grade_in >= 73:
    letter = 'C'
elif grade_in < 73 and grade_in >= 70:
    letter = 'C-'
elif grade_in < 70 and grade_in >= 67:
    letter = 'D+'
elif grade_in < 67 and grade_in >= 63:
    letter = 'D'
elif grade_in < 63 and grade_in >= 60:
    letter = 'D-'
elif grade_in < 60:
    letter = 'F'

    
print(f'Grade: {letter}')
if grade_in >= 70:
    print('You passed the class!')
else:
    print('You failed the class but you can always try again.')


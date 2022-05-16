import math

grade_in = float(input('What is your grade (0-100)?: '))
grade = 'A+'
if grade_in >= 97:
    grade = 'A+'
elif grade_in < 97 and grade_in >= 93:
    grade = 'A'
elif grade_in < 93 and grade_in >= 90:
    grade = 'A-'
elif grade_in < 90 and grade_in >= 87:
    grade = 'B+'
elif grade_in < 87 and grade_in >= 83:
    grade = 'B'
elif grade_in < 83 and grade_in >= 80:
    grade = 'B-'
elif grade_in < 80 and grade_in >= 77:
    grade = 'C+'
elif grade_in < 77 and grade_in >= 73:
    grade = 'C'
elif grade_in < 73 and grade_in >= 70:
    grade = 'C-'
elif grade_in < 70 and grade_in >= 67:
    grade = 'D+'
elif grade_in < 67 and grade_in >= 63:
    grade = 'D'
elif grade_in < 63 and grade_in >= 60:
    grade = 'D-'
elif grade_in < 60 and grade_in >= 57:
    grade = 'F+'
elif grade_in < 57 and grade_in >= 53:
    grade = 'F'
elif grade_in < 53:
    grade = 'F-'
else:
    print('Invalid Input')

print(f'You have a {grade}')

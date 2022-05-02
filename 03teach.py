import math

squareLength = input('What is the length of a side of the square?: ')
floatSquareLength = float(squareLength)
squareArea = floatSquareLength ** 2
print(f'The area of the square is: {squareArea} units squared')

width = input('What is the width of the rectangle?: ')
floatWidth = float(width)
length = input('What is the length of the rectangle?: ')
floatLenght = float(length)
area = floatLenght * floatWidth
print(f'The area of the rectangle is: {area} units squared')

radius = input('What is the radius of the circle?: ')
floatRadius  = float(radius)
areaCircle = math.pi * floatRadius ** 2
print(f'The area of the circle is: {areaCircle} units squared')

value = input('Input a value: ')
floatValue = float(value)
areaSquare = floatValue ** 2
cubeVolume = floatValue ** 3
circleArea = math.pi * floatValue ** 2
print(f'The area of a square with the side length of {value} is {areaSquare} units squared.' )
print(f'The volume of a square with the side length of {value} is {cubeVolume} units cubed.' )
print(f'The area of a circle with the a radius length of {value} is {areaSquare} units squared.' )


import math

wind_speed = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
temp = float(input('What is the temperature?: '))

unit = input('Fahrenheit or Celsius (F/C)?: ')

while unit.lower() != 'f' and unit.lower() != 'c':
    print('INVALID INPUT')
    unit = input('Fahrenheit or Celsius (F/C)?: ')

if unit.lower() == 'c':
    temp = (temp * 9/5) + 32

for i, e in enumerate(wind_speed):
    windchill = 35.74 + 0.6215 * temp - 35.75 * (wind_speed[i] ** 0.16) + 0.4275 * temp * (wind_speed[i] ** 0.16)
    print(f'At temperature {temp}F, and wind speed {wind_speed[i]} mph, the windchill is: {windchill: .2f}')
import csv

rows = []


with open('life-expectancy.csv', 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)

omin = rows[0][3]
omax = rows[0][3]

for i in range(len(rows)):
    if rows[i][3] < omin:
        omin = rows[i][3]

for i in range(len(rows)):
    if rows[i][3] > omax:
        omax = rows[i][3]


print(omin)
print(omax)

year = input('Enter the year of interest: ')
yoi_list = []

for i in range(len(rows)):
    if rows[i][2] == str(year):
        yoi_list.append(rows[i])

yoi_min = yoi_list[0][3]
yoi_min_country = yoi_list[0][0]
yoi_max = yoi_list[0][3]
yoi_max_country = yoi_list[0][0]

for i in range(len(yoi_list)):
    if yoi_list[i][3] < yoi_min:
        yoi_min = yoi_list[i][3]
        yoi_min_country = yoi_list[i][0]

for i in range(len(yoi_list)):
    if yoi_list[i][3] > yoi_max:
        yoi_max = yoi_list[i][3]
        yoi_max_country = yoi_list[i][0]

print(f'For the year {year}:\nThe average life expectancy across all countries was: \nThe minimum life expectancy was in {yoi_min_country} at: {yoi_min} years\nThe maximum life expectancy was in {yoi_max_country} at: {yoi_max} years')





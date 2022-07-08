import csv

rows = []


with open('life-expectancy.csv', 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)

omin = rows[0][3]
omin_country = rows[0][0]
omin_year = rows[0][2]
omax = rows[0][3]
omax_country = rows[0][0]
omax_year = rows[0][2]

for i in range(len(rows)):
    if rows[i][3] < omin:
        omin = rows[i][3]
        omin_country = rows[i][0]
        omin_year = rows[i][2]

for i in range(len(rows)):
    if rows[i][3] > omax:
        omax = rows[i][3]
        omax_country = rows[i][0]
        omax_year = rows[i][2]



year = input('Enter the year of interest: ')
yoi_list = []

for i in range(len(rows)):
    if rows[i][2] == str(year):
        yoi_list.append(rows[i])


yoi_min = yoi_list[0][3]
yoi_min_country = yoi_list[0][0]
yoi_max = yoi_list[0][3]
yoi_max_country = yoi_list[0][0]
yoi_avg = 0

for i in range(len(yoi_list)):
    yoi_avg += float(yoi_list[i][3])

yoi_avg = yoi_avg/len(yoi_list)


for i in range(len(yoi_list)):
    if yoi_list[i][3] < yoi_min:
        yoi_min = yoi_list[i][3]
        yoi_min_country = yoi_list[i][0]

for i in range(len(yoi_list)):
    if yoi_list[i][3] > yoi_max:
        yoi_max = yoi_list[i][3]
        yoi_max_country = yoi_list[i][0]

print()
print(f'The overall minimum life expectancy is: {omin} from {omin_country} in {omin_year}\nThe overall maximum life expectancy is: {omax} from {omax_country} in {omax_year}')
print()
print(f'For the year {year}:\n\nThe average life expectancy across all countries was: {yoi_avg: .3f} years\nThe minimum life expectancy was in {yoi_min_country} at: {yoi_min} years\nThe maximum life expectancy was in {yoi_max_country} at: {yoi_max} years')





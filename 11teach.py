from inspect import cleandoc


with open('hr_system.txt') as file:
    for line in file:
        clean_line = line.strip()
        line_list = clean_line.split(' ')
        

        if line_list[2] == 'Engineer':
            name = line_list[0]
            id = line_list[1]
            job = line_list[2]
            line_list[3] = float(line_list[3])
            monthly = line_list[3]/24
            bonus = monthly + 1000
            print(f'{name} (ID: {id}), {job} - ${bonus:.2f}')
        else:
            name = line_list[0]
            id = line_list[1]
            job = line_list[2]
            line_list[3] = float(line_list[3])
            monthly = line_list[3]/24
            print(f'{name} (ID: {id}), {job} - ${monthly:.2f}')



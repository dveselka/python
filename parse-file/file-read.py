import csv

select_text = 'select C1, C2, C3 from T1 where C1 in (';

union_text = 'union all'

with open('input.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
 
        if line_count > 0 and line_count % 5  == 0:
            print(')')
            print(union_text)
        if line_count % 5  == 0:
            print(select_text)

        print(f'\'{row[0]}\'', end='')
        if line_count % 5  < 4 :
            print(',')
        
        line_count += 1
    print(')')


import os
from calendar import monthrange
import csv

def flatten(l):
    return [item for sublist in l for item in sublist]

def format_row(raw_row,month,year):
    row = []
    for str_elem in flatten(raw_row):
        try:
            num_elem = int(str_elem)
        except:
            try:
                num_elem = float(str_elem)
            except:
                num_elem = float('nan')
        row.append(num_elem)
    row[0] = f'{month:02}/{row[0]:02}/{year}'
    return row

abrv = 'CHI'

files_list = list(os.listdir(f'{abrv}_weather_data_files'))

with open(f'{abrv}_weather_data.csv', 'w', newline='\n') as write_file:
    writer = csv.writer(write_file)
    writer.writerow(['date', 'hi_temp', 'avg_temp', 'lo_temp', 'hi_dp', 'avg_dp',
        'lo_dp', 'hi_hum', 'avg_hum', 'lo_hum', 'hi_wind', 'avg_wind', 'lo_wind',
        'hi_pres', 'avg_pres', 'lo_pres', 'hi_precip', 'avg_precip', 'lo_precip'])
    for filename in files_list:
        year = int(filename[4:8])
        month = int(filename[9:11])
        days_in_month = monthrange(year,month)[1]
        
        with open(f'{abrv}_weather_data_files/{filename}') as read_file:
            lines = [line.strip('\n') for line in read_file]
            group_size = days_in_month+1 # +1 accounts for headers
            number_of_groups = -(len(lines)//-group_size)
            # this double negative expression is just a ceiling division hack
            # i.e. floor division: x//y, ceiling division: -(x//-y)
            
            grouped = []
            for g in range(number_of_groups):
                new_group = lines[group_size*g:group_size*(g+1)]
                grouped.append([chunk.split(' ') for chunk in new_group[1:]])
            for raw_row in list(zip(*grouped)):
                row = format_row(raw_row,month,year)
                writer.writerow(row)
import os
import pandas as pd
from calendar import monthrange
import csv

print(os.getcwd())

all_files = list(os.listdir('CHI_weather_data'))
try:
    all_files.remove('.DS_Store')
except:
    pass
all_files.sort(reverse = True)

for file in all_files:
    year = int(float(file[4:8]))
    month = int(float(file[9:11]))
    row_multiple = monthrange(year,month)[1] + 1
#     if file == 'CHI-2018-3.txt':
#         row_multiple = 26 + 1
    raw_lines = []
    for line in open('CHI_weather_data/'+file):
        if line[-1]=='\n':
            raw_lines.append(line[:-1])
        else:
            raw_lines.append(line)
    
    print('read','CHI_weather_data/'+file)
    ordered_lines = []
    for n in range(row_multiple):
        ordered_lines.append(raw_lines[n+0*row_multiple].split(' ') + raw_lines[n+1*row_multiple].split(' ')
                           + raw_lines[n+2*row_multiple].split(' ') + raw_lines[n+3*row_multiple].split(' ')
                           + raw_lines[n+4*row_multiple].split(' ') + raw_lines[n+5*row_multiple].split(' ')
                           + raw_lines[n+6*row_multiple].split(' '))

    header_list = ['Date', 'Temperature (° F)', 'Temperature (° F)', 'Temperature (° F)',
                   'Dew Point (° F)', 'Dew Point (° F)', 'Dew Point (° F)', 'Humidity (%)',
                   'Humidity (%)', 'Humidity (%)', 'Wind Speed (mph)', 'Wind Speed (mph)',
                   'Wind Speed (mph)', 'Pressure (Hg)', 'Pressure (Hg)', 'Pressure (Hg)',
                   'Precipation (in)', 'Precipation (in)', 'Precipation (in)']
    
    data_array = [[]]
    for subheader, header in zip(ordered_lines[0],header_list):
        data_array[0].append(subheader+' '+header)
        
    data_array[0][0] = 'Date'
    for line in ordered_lines[1:]:
        day = int(line[0])
        data_array.append(['{year:04d}-{month:02d}-{day:02d}'.format(year=year,month=month,day=day)]+line[1:])
    
    filename = 'CHI-{year:04d}-{month:02d}_processed.csv'.format(year=year,month=month)

    with open('processed_CHI_files/'+filename, 'w', newline='', encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerows(data_array)
    print('wrote','processed_CHI_files/'+filename+'\n')

# import os
# import pandas as pd
# from calendar import monthrange
# import csv
# import datetime
# # import seaborn as sns

# chi_files = list(os.listdir('processed_CHI_files'))

# # try:
# #     chi_files.remove('.DS_Store')
# # except:
# #     pass
# chi_files.sort()

# print(chi_files)



import os
import pandas as pd
from calendar import monthrange
import csv

print(os.getcwd())

all_files = list(os.listdir('CHI_weather_data'))
print(all_files)
# chi_weather_data = pd.DataFrame()

# for file in chi_files:
#     df_chunk = pd.read_csv('processed_CHI_files/'+file)
#     print('Chunk dims for', file, ': ', df_chunk.shape)
#     chi_weather_data = pd.concat([chi_weather_data, df_chunk], ignore_index=True)

# print('Total Chicago dataframe dimensions:',chi_weather_data.shape,'\n')

# chi_weather_data.to_csv('chicago_weather.csv')

# chi_ridership_data = pd.read_csv('CTA_Daily_Boarding_Totals.csv')
# chi_ridership_data['service_date'] = pd.to_datetime(chi_ridership_data['service_date'])

# # Join tables, using 'service_date' and 'Date' as index keys
# all_chi_data = chi_ridership_data[['service_date','day_type','total_rides']]\
#             .set_index('service_date').join(chi_weather_data.set_index('Date'))
# chi_data = all_chi_data[181:] # drop rows with missing weather data
# chi_data = pd.concat([chi_data, pd.get_dummies(chi_data['day_type'], prefix='is')],
#                      axis=1).drop(['day_type'],axis=1).drop(['is_W'],axis=1)

# chi_data = chi_data.drop(['Avg Temperature (° F)'],axis=1)\
#                    .drop(['Avg Dew Point (° F)'],axis=1)\
#                    .drop(['Avg Humidity (%)'],axis=1)\
#                    .drop(['Avg Wind Speed (mph)'],axis=1)\
#                    .drop(['Avg Pressure (Hg)'],axis=1)\
#                    .drop(['Max Precipation (in)'],axis=1)\
#                    .drop(['Min Precipation (in)'],axis=1)

# chi_data['Temperature Variation (° F)'] = chi_data['Min Temperature (° F)'] - chi_data['Max Temperature (° F)']
# chi_data = chi_data.drop(['Min Temperature (° F)'],axis=1)

# chi_data['Dew Point Variation (° F)'] = chi_data['Min Dew Point (° F)'] - chi_data['Max Dew Point (° F)']
# chi_data = chi_data.drop(['Min Dew Point (° F)'],axis=1)

# chi_data['Humidity Variation (%)'] = chi_data['Min Humidity (%)'] - chi_data['Max Humidity (%)']
# chi_data = chi_data.drop(['Min Humidity (%)'],axis=1)

# chi_data['Wind Speed Variation (mph)'] = chi_data['Min Wind Speed (mph)'] - chi_data['Max Wind Speed (mph)']
# chi_data = chi_data.drop(['Min Wind Speed (mph)'],axis=1)

# chi_data['Pressure Variation (Hg)'] = chi_data['Min Pressure (Hg)'] - chi_data['Max Pressure (Hg)']
# chi_data = chi_data.drop(['Min Pressure (Hg)'],axis=1)

# chi_data = chi_data.rename(index=str, columns={
#     'Max Temperature (° F)': 'max_temp',
#     'Max Dew Point (° F)': 'max_dew_pt',
#     'Max Humidity (%)': 'max_hum',
#     'Max Wind Speed (mph)': 'max_wind',
#     'Max Pressure (Hg)': 'max_pres',
#     'Avg Precipation (in)': 'precip',
#     'is_A': 'is_sat',
#     'is_U': 'is_holi',
#     'Temperature Variation (° F)': 'temp_var',
#     'Dew Point Variation (° F)': 'dew_pt_var',
#     'Humidity Variation (%)': 'hum_var',
#     'Wind Speed Variation (mph)': 'wind_var',
#     'Pressure Variation (Hg)': 'pres_var'})

# chi_data.to_csv('chi_data.csv')
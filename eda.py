import pandas as pd
import csv

abrv = 'CHI'

chi_weather_data = pd.read_csv(f'{abrv}_weather_data.csv')

chi_weather_data.drop(['avg_hum','avg_wind','avg_pres','hi_precip','lo_precip'],
		axis=1, inplace=True)

chi_weather_data.hist(bins=10)

# print(list(chi_weather_data))#
# print(chi_weather_data.info())
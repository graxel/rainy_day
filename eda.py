import pandas as pd
import csv
import matplotlib.pyplot as plt

abrv = 'CHI'

chi_weather_data = pd.read_csv(f'{abrv}_weather_data.csv', index_col='date', parse_dates=True)

chi_ridership_data = pd.read_csv('CTA_Daily_Boarding_Totals.csv', index_col='service_date', parse_dates=True)

chi_data = chi_ridership_data.join(chi_weather_data)

# drop empty columns
chi_data.drop(['avg_hum','avg_wind','avg_pres','hi_precip','lo_precip'], axis=1, inplace=True)

# drop days with erroneous data; happens to be last two data points
chi_data.drop(chi_data['2018-06-29':].index, axis=0, inplace=True)

# check distributions of features using histograms
pd.DataFrame.hist(data=chi_data, figsize=(10,10), layout=(4,4), bins=15)

plt.show()

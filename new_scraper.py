import time
import pandas as pd
import selenium
from datetime import datetime
from selenium import webdriver
import os
import random


def read_webpage(driver,url):
        
    driver.get(url)

    # pause for a few seconds to let page load
    time.sleep(random.randint(5,12))

    xp = '//app/city-history/city-history-layout/div/div[2]/'\
            + 'section/div[2]/div[3]/div/div/div/div/'\
            + 'city-history-observation/div/div[2]/table/tbody'
    
    webpage_data = driver.find_element_by_xpath(xp)

    return webpage_data

driver = webdriver.Chrome()

# Generate list of dates (months) to pull weather data for.

# For Chicago
city = 'il/chicago/KORD'
abrv = 'CHI'
start_date = datetime(2018,10,1)
end_date = datetime(2018,12,1)

date_list = pd.Series(pd.date_range(start_date,end_date,freq='MS'))

# idempotently create directory for weather data
w_data_dir = f'{abrv}_weather_data'
os.makedirs(w_data_dir, exist_ok = True)

for date in date_list:
    
    url = f'https://www.wunderground.com/history/monthly/us/{city}/date/{date.year}-{date.month}?cm_ven=localwx_history'
    
    # Record start time (for scraper performance purposes)
    start_time = datetime.now()
    webpage_data = read_webpage(driver, url)

    storage = open(f'{w_data_dir}/{abrv}-{date.year}-{date.month}.txt', 'w')
    
    storage.write(webpage_data.text)
    
    stop_time = datetime.now()
    elapsed = stop_time-start_time

    print('Weather data for ',date.month,'/',date.year,' scraped in ',
          elapsed.seconds + elapsed.microseconds/1000000, ' s', sep='')

driver.close()
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import selenium
from datetime import datetime
from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import csv
import random


def read_webpage(driver,url):
        
    driver.get(url)

    time.sleep(random.randint(5,12))
    xp = '//app/city-history/city-history-layout/div/div[2]/'\
            + 'section/div[2]/div[3]/div/div/div/div/'\
            + 'city-history-observation/div/div[2]/table/tbody'
    
    webpage_data = driver.find_element_by_xpath(xp)

    return webpage_data


# chromedriver = '/Users/grazillionaire/Documents/chromedriver' # path to the chromedriver executable
# os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome()


# Generate list of dates (months) to pull weather data for.

# For Chicago
city = 'il/chicago/KORD'
start_date = datetime(2006,6,1)
end_date = datetime(2018,12,1)


# For New York
#city = 'ny/new-york/KNYC'
#start_date = datetime(2010,5,1)
#end_date = datetime.today()

date_list = pd.Series(pd.date_range(start_date,end_date,freq='MS'))

for date in date_list:
    
    url = 'https://www.wunderground.com/history/monthly/us/{loc}/date/{y}-{m}?cm_ven=localwx_history'\
          .format(loc=city, y=date.year, m=date.month)
    
    # Record start time (for scraper performance purposes)
    start_time = datetime.now()
    webpage_data = read_webpage(driver, url)

    storage = open('CHI weather data/CHI-{y}-{m}.txt'\
                  .format(y=date.year, m=date.month), 'w')
    
    storage.write(webpage_data.text)
    
    stop_time = datetime.now()
    elapsed = stop_time-start_time

    print('New weather data for ',date.month,'/',date.year,' scraped in ',
          elapsed.seconds + elapsed.microseconds/1000000, ' s', sep='')

driver.close()
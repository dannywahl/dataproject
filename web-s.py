import requests
import pickle
from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd

def url_to_ts(url)
  '''Returns latest 24h of Nord Pools spot prices'''
  page = requests.get(url).text
  soup = BeautifulSoup(page,"lxml")
  data_tmp = [p.text for p in soup.find(class_="ng-scope").find_all('p')]

ts_today = url_to_ts('https://www.nordpoolgroup.com/Market-data1/Dayahead/Area-Prices/ALL1/Hourly/?view=table')

mkdir ts_pickled_2020_05_04
with open("ts_pickled_2020_05_04/"+0+".txt","rb") as file:
  pickle.dump(ts_today[0], file)


data = {}
with open("ts_pickled_2020_05_04/"+0+".txt","rb") as file:
  data[0] = pickle.load(file)


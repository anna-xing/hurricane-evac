import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
from urllib.request import urlopen
from __main__ import *

url = "http://ibtracs.unca.edu/index.php?name=v04r00-2018280N18273"
html = urlopen(url)

soup = BeautifulSoup(html, 'lxml')

tables = soup.find_all('table')

def extract_storm_data():
    i = 0
    for table in tables:
        if i == 3:
            return table
        else:
            i += 1


storm_data_table = extract_storm_data()

storm_data_rows = storm_data_table.find_all('tr')

list_of_rows = []

for row in storm_data_rows:
    row_td = row.find_all('td')
    clean_row = BeautifulSoup(str(row_td), "lxml").get_text()
    list_of_rows.append(clean_row)

df = pd.DataFrame(list_of_rows)
df1 = df[0].str.split(',', expand=True)
df1 = df1.drop([0, 2, 5, 6, 8], axis=1)
df1.columns = ['Time', 'Lat', 'Lon', 'Wind']
df1 = df1.drop([0, 1])
df1 = df1.reset_index(drop=True)

df1['Wind'] = np.round(df1['Wind'].apply(int) * 1.151)
df1['Lat'] = np.deg2rad(df1['Lat'].apply(float))
df1['Lon'] = np.deg2rad(df1['Lon'].apply(float))

# def haversine(df):
#     i = 1
#     index_length = len(df.index)
#     dist = []
#     for i in range(1, index_length):
#         second = i
#         first = i - 1
#         delta_lat = float(df.iloc[second, 1]) - float(df.iloc[first, 1])
#         delta_lon = float(df.iloc[second, 2]) - float(df.iloc[first, 2])
#         a = np.square(np.sin(delta_lat / 2)) + np.cos(float(df.iloc[first, 1])) * np.cos(float(df.iloc[second, 1])) * np.square(np.sin(delta_lon / 2))
#         c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
#         d = np.round(6371 * c)
#         dist.append(d)
#         i += 1
#         return dist
#
# print(len(df.index))
# distance = haversine(df1)
# print(df1)
# df1 = haversine(df1)
# print(df1)
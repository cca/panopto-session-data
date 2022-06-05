import sqlite3

import pandas as pd

conn = sqlite3.connect('pano.db')
# load the data into a Pandas DataFrame
sessions = pd.read_csv('sessionscreatedoredited_2020-08-08--2022-06-01.csv', low_memory=False)
# write the data to a sqlite table
sessions.to_sql('sessions', conn, if_exists='append', index=False)

usage = pd.read_csv('sessionusage_2020-08-08--2022-06-01.csv', low_memory=False)
usage.to_sql('sessions', conn, if_exists='append', index=False)
conn.close()

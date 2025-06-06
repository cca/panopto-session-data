import sqlite3

import pandas as pd

conn = sqlite3.connect("pano.db")
# load the data into a Pandas DataFrame
sessions = pd.read_csv("sessionscreatedoredited.csv", low_memory=False)
# write the data to a sqlite table
sessions.to_sql("sessions", conn, if_exists="replace", index=False)

usage = pd.read_csv("sessionusage.csv", low_memory=False)
usage.to_sql("usage", conn, if_exists="replace", index=False)
conn.close()

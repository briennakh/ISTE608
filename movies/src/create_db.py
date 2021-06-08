# Dataset is from https://www.kaggle.com/rounakbanik/the-movies-datasethttps://www.kaggle.com/rounakbanik/the-movies-dataset

import pandas as pd
import sqlite3

root = './movies/'

# Create a database connection and cursor to execute queries
conn = sqlite3.connect(root + 'data/movies.db')
c = conn.cursor()

# Load the data into a Pandas DataFrame
metadata_df = pd.read_csv(root + 'data/movies_metadata.csv')

# Write the data to a sqlite table
metadata_df.to_sql('metadata', conn, if_exists='replace', index=False) # CAREFUL: 'replace' is used here because I don't care about the data integrity, as this is practice
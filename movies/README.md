
# Movies 

In this repo, I explore a movie database, to answer some questions such as...

1. Which genres are the most popular? How has this popularity changed over time, e.g. 2000 vs. 2015?
2. What attributes are associated with movies that have the highest revenue?

## Files
- `./data/` — Contains all the data, which is not versioned due to GitHub file size limits. The CSVs can be downloaded from [Kaggle](https://www.kaggle.com/rounakbanik/the-movies-datasethttps://www.kaggle.com/rounakbanik/the-movies-dataset), and the sqlite3 database is created using `./src/create_db.py`

- `./src/` — Contains all the code
  - `create_db.py` — Creates sqlite3 database from CSV files
    - A [resource](https://stackoverflow.com/questions/305378/list-of-tables-db-schema-dump-etc-using-the-python-sqlite3-api/33100538#33100538) on doing the opposite
  - `explore_db.py` — Explores the sqlite3 database
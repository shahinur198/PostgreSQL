# ----- Example Python program to create a database in PostgreSQL using Psycopg2 -----

# import the PostgreSQL client for Python

import psycopg2

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Connect to PostgreSQL DBMS

conn = psycopg2.connect(user = "postgres", password = "test123", host = "127.0.0.1", port = "5432")

conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Obtain a DB Cursor

cursor          = conn.cursor()

name_Database   = "online_class_db";

# Create table statement

sqlCreateDatabase = "create database "+name_Database+";"

# Create a table in PostgreSQL database

cursor.execute(sqlCreateDatabase)

conn.close()
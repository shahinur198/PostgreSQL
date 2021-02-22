import psycopg2

conn = psycopg2.connect(database = "mtdb", user = "postgres", password = "test123", host = "127.0.0.1", port = "5432")
print ("Opened database successfully")

cur = conn.cursor()
user_table = ''' CREATE TABLE IF NOT EXISTS tblUsers (
                                            user_id INT PRIMARY KEY,
                                            name CHAR(50) NOT NULL,
                                            gender CHAR(50) NOT NULL,
                                            date_of_birth REAL,
                                            profile_pic CHAR(50),
                                            create_date REAL,
                                            status bool NOT NULL
                                        ); '''
# user_table = '''CREATE TABLE IF NOT EXISTS COMPANY1
# 										      (ID INT PRIMARY KEY     NOT NULL,
# 										      NAME           TEXT    NOT NULL,
# 										      AGE            INT     NOT NULL,
# 										      ADDRESS        CHAR(50),
# 										      SALARY         REAL);'''
cur.execute(user_table)
print ("Table created successfully")

conn.commit()
conn.close()
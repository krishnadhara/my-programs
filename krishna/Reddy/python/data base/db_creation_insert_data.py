import psycopg2
import sys
connection=psycopg2.connect(database="libdb",user = "postgres",password ="1234", host = "127.0.0.1", port = "5432")
curs=connection.cursor()
curs.execute("DROP TABLE IF EXISTS EMPLOY ")
curs.execute(''' CREATE TABLE EMPLOY
            (ID      INT     PRIMARY KEY NOT NULL,
             NAME     TEXT              NOT NULL,
             AGE      INT               NOT NULL,
             ADDRESS  CHAR(10),
             SALARY    REAL)''')
curs.execute("INSERT INTO EMPLOY (ID,NAME,AGE,ADDRESS,SALARY) \
             VALUES (1, 'Paul', 32, 'California', 20000.00 )");
curs.execute("INSERT INTO EMPLOY (ID,NAME,AGE,ADDRESS,SALARY) \
             VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
curs.execute("INSERT INTO  EMPLOY (ID,NAME,AGE,ADDRESS,SALARY) \
             VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
curs.execute("INSERT INTO  EMPLOY (ID,NAME,AGE,ADDRESS,SALARY) \
             VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
connection.commit()
connection.close()
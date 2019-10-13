import psycopg2
connection=psycopg2.connect(database="libdb", user = "postgres",password ="1234", host = "127.0.0.1", port = "5432")
cur=connection.cursor()
cur.execute(''' CREATE TABLE COMPANY
            (ID      INT     PRIMARY KEY NOT NULL,
             NAME     TEXT              NOT NULL,
             AGE      INT               NOT NULL,
             ADDRESS  CHAR(50),
             SALORY    REAL);''')
connection.commit()
connection.close()


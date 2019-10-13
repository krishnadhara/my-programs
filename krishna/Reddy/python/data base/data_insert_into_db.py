import psycopg2
connection=psycopg2.connect(database="libdb",user = "postgres",password ="1234", host = "127.0.0.1", port = "5432")
cur=connection.cursor()
cur.execute("DROP TABLE IF EXISTS COMPANY")
cur.execute(''' CREATE TABLE COMPANY
            (ID      INT     PRIMARY KEY NOT NULL,
             NAME     TEXT              NOT NULL,
             AGE      INT               NOT NULL,
             ADDRESS  CHAR(50),
             SALORY    REAL)''')
cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALORY) \
            VALUES (1,'KRISHNA',24,'INDIA',20000.00)");
cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALORY) \
             VALUES (2,'DHARA',20,'JAPAN',25000.00)");
cur.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALORY) \
             VALUES(3,'sushmtha',18,'united states',50000.00)");
cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALORY) \
            VALUES (4,'KRISHNA',24,'INDIA',20000.00)");
cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALORY) \
             VALUES (5,'DHARA',20,'JAPAN',25000.00)");
cur.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALORY) \
             VALUES(6,'sushmtha',18,'united states',50000.00)");
connection.commit()
connection.close()

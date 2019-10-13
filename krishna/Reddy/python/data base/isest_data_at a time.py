import psycopg2
import sys
cars=((1,'audi',52642),(2,'benz',52643),(3,'skods',52644),(4,'tata',526467),
      (5,'hero',526421),(6,'bajaj',5264209),(7,'honda',5264207),(8,'hundai',5902642),
      (9,'scoda',526402),(10,'hitachi',526412),(11,'volva',526142),(12,'pulsar',52642),
      (13, 'Audi', 52642), (14, 'Mercedes', 57127), (15, 'Skoda', 9000),
      (16, 'Volvo', 29000), (17, 'Bentley', 350000), (18, 'Citroen', 21000),
      (19, 'Hummer', 41400), (20, 'Volkswagen', 21600)
      )
try:
    connection=psycopg2.connect(database="libdb", user = "postgres",
                                password ="1234", host = "127.0.0.1", port = "5432")
    cur=connection.cursor()
    cur.execute("DROP TABLE IF EXISTS cars")
    cur.execute("CREATE TABLE cars(Id INT PRIMARY KEY, Name TEXT,Price INT)")
    query="INSERT INTO cars(Id,Name,Price) VALUES (%s,%s,%s)"
    cur.executemany(query,cars)
    connection.commit()
except psycopg2.DatabaseError as e:
    if connection:
        connection.rollback()
    print ('error %s' %e)
    sys.exit(1)
finally:
    if connection:
        connection.close()

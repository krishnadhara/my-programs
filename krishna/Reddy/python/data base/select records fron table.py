import psycopg2
connection=psycopg2.connect(database="libdb", user = "postgres",password ="1234", host = "127.0.0.1", port = "5432")
cur=connection.cursor()
cur.execute("select id ,name,address,salory from company")
#rows=cur.fetchall()
#print(rows)
rows=cur.fetchone()
print(rows)
connection.close()
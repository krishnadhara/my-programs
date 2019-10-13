import psycopg2
connection=psycopg2.connect(database="libdb", user = "postgres",password ="1234", host = "127.0.0.1", port = "5432")
cur=connection.cursor()
cur.execute("update company set salory =25000.00 where id=1")
connection.commit()
cur.execute("select id,name,address,salory from company")
rows=cur.fetchall()
print(rows)
connection.close()
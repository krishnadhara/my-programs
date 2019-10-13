import psycopg2
connection=psycopg2.connect(database="libdb", user = "postgres",password ="1234", host = "127.0.0.1", port = "5432")

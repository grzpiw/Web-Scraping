import psycopg2

db_password = "postgres"
db_user = "postgres"

# =========================================================================================
create_query = "create table abc (a integer, b integer)"
conn = psycopg2.connect(dbname="postgres", user=db_user, password=db_password, host="localhost")
cur = conn.cursor()

cur.execute(create_query)
conn.commit()

insert_query = "INSERT INTO abc(a, b) VALUES(1, 2)"
cur.execute(insert_query)
conn.commit()

cur.close()
conn.close()

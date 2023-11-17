import json


credentials = json.load( open( "credentials.json", "r" ) )

dbname = credentials["dbname"]
user = credentials["username"]
password = credentials["password"]
host = credentials["host"]



# CREATE
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
cur = conn.cursor()


create_query = '''
CREATE TABLE transactions (
    id SERIAL,
    client_id VARCHAR(12),
    value NUMERIC(5) NOT NULL,
    products TEXT NOT NULL,
    datetime TIMESTAMP NOT NULL,
    cashier_nr SMALLINT NOT NULL
    );
'''

cur.execute(create_query)
conn.commit()


cur.close()
conn.close()

# INSERT
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
cur = conn.cursor()



insert_query = '''INSERT INTO transactions(client_id, value, products, datetime, cashier_nr) VALUES ( 'G3O6R',90.45728312600907,'6WBYOW2A3LBJ9DZOH747TJQE86512DXCMWETRVG77T7EBBYG3K','2019-4-19',53);
INSERT INTO transactions(client_id, value, products, datetime, cashier_nr) VALUES ( '9T738',38.00585995390484,'I88I7EZ28XVX4KEYMVZWTHYYDMEO79218E855D2X31PYI30DNR','2020-6-11',27);
INSERT INTO transactions(client_id, value, products, datetime, cashier_nr) VALUES ( '3T66N',64.4065978416009,'DTLFD9KMKY0ANV043TESYBEDLSGKEDMVP7571IDAUGX4LCJXZ5','2019-8-4',65);
INSERT INTO transactions(client_id, value, products, datetime, cashier_nr) VALUES ( 'A06WI',39.95964442587763,'10F3ODRGNKYXBYBIOM7MKRNZJMSM9Z7KDKWUJ1C609I8U2JG82','2018-9-5',58);
INSERT INTO transactions(client_id, value, products, datetime, cashier_nr) VALUES (NULL,17.630978858138224,'5IQVEQI0PI0ACJH2PEKMZX94S3E6AMQBUINBPRQQN7LRRFB8V1','2019-10-30',20);
INSERT INTO transactions(client_id, value, products, datetime, cashier_nr) VALUES (NULL,65.8281418616092,'I981MRPDHEHDL0CJHI6NRNJ0SJX8X4T75R4W3XXI34QZXMU866','2020-8-3',5);
INSERT INTO transactions(client_id, value, products, datetime, cashier_nr) VALUES ( 'XBAT5',22.76245244569366,'EAM37LUA2V62914RA2GKPZ509XJJ7TNXJNMZ95S8CLZ62GEZAZ','2019-4-16',62);
INSERT INTO transactions(client_id, value, products, datetime, cashier_nr) VALUES (NULL,96.62388915769743,'O9GHBAKU1NRJSNRLTACOY43XXQ62P17SHSV64TZN2J8KTUKPON','2018-11-26',29);
INSERT INTO transactions(client_id, value, products, datetime, cashier_nr) VALUES ( 'GQFD5',92.39568764245556,'1FPTZ60BNTRBMZXO4WSL8T2KYGMWUCPVQ2Q2TS0RC1YPRS5HKX','2020-8-3',33);
INSERT INTO transactions(client_id, value, products, datetime, cashier_nr) VALUES (NULL,63.40658956106905,'VV2ZMUS1BZQ9JS5SGJS0XL2LDUGD9FIIJGMJ29E7VJB83QMCWH','2019-2-24',61);'''


cur.execute(insert_query)
conn.commit()

cur.close()
conn.close()

# SELECT
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
cur = conn.cursor()


select_query = '''
SELECT * FROM transactions
'''

cur.execute(select_query)
result = cur.fetchall()

cur.close()
conn.close()


# DELETE

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
cur = conn.cursor()


delete_query = '''DELETE FROM transactions'''

cur.execute(delete_query)
conn.commit()

cur.close()
conn.close()

# DROP
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
cur = conn.cursor()

drop_query = '''
DROP TABLE transactions
'''

cur.execute(drop_query)
conn.commit()

cur.close()
conn.close()

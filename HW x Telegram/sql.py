import MySQLdb
def quer(conn):
	cur=conn.cursor()
	cur.execute("SELECT count(*) FROM sakila.film_actor;")
	for val in cur.fetchall():
		print(val)
cnx= MySQLdb.connect(host='localhost',user='root',passwd='357951',db='sakila')
quer(cnx)
cnx.close
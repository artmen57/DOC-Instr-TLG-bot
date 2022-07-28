from mysql.connector import Error,connect
cfg=	{'user':'root',
		'password':'357951',
		'host':'localhost'}
try:
	cnx = connect(**cfg)
	print("Connection to",cfg['host'],"from",cfg["user"],"is successfully.")
	console = cfg['host']+"@"+cfg["user"]
except Error as e:
	print (e)


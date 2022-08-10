from mysql.connector import Error,connect
from math import ceil
cfg=	{'user':'root',
		'password':'357951',
		'host':'localhost'}
menu = 	{1: "Show menu",
		 2: "Use DB",
		 3: "Show info about DB's / tables in DB",
		 4: "Select data",
		 5: "Drop DB / table in DB",
		 6: "Create DB / table in DB",
		 7: "Insert row",
		 9: "Free SQL",
		 0: "Exit"}

def show_menu():
	print("MySQL API main menu:")
	for key, item in menu.items():
		print("%d. %s"%(key, item))

def sql(query=""):
	if query == "":
		query = input("sql_query::%s>"%(console))
	try:
		curs=cnx.cursor()
		curs.execute(query)
		answer_rows=curs.fetchall()
		if answer_rows:
			answer_desc = curs.description
			i = 0
			max_lens = []
			max_len_rows = []
			print()
			for desc in answer_desc:
				for rows in answer_rows:
					max_lens.append(len(str(rows[i])))
				max_lens.append(len(str(desc[0])))
				max_len = max(max_lens)
				max_len_rows.append(max_len)
				print(str(desc[0]).ljust(max_len), end=" |")
				i += 1
			print()
			print("".rjust(sum(max_len_rows)+ceil(sum(max_len_rows)*8.77/100),'-'))
			for rows in answer_rows:
				i = 0
				for row in rows:
					print(str(row).ljust(max_len_rows[i]),end=" |")
					i += 1
				print()
		print("Query OK, Total rows:", curs.rowcount);cnx.commit()
		return 1
	except Error as e:
		print(e)
		return 0

def show_info():
	print("1. Show databases","2. Show tables","0. Back",sep="\n")
	try:
		print("show_info::%s>"%(console), end="")
		index = int(input())
		match index:
			case 1:
				sql("show databases;")
			case 2:
				sql("show tables;")
			case 0:
				return
			case _:
				print('Unknown command. Try again')
	except ValueError as ve:
		print("Index Error (%s)"%(ve))

def select():
	query = "select "
	table = input("Name of table: ")
	index = input("Select all rows of table?[y/n]: ")
	if index == "n":
		while True:
			column = input("Column: ")
			query += "%s"%(column)
			index = input("Add column?[y/n]: ")
			if index == "n":
				break
			query += ", "
	else:
		query += "*"
	query += " from %s;"%(table)
	sql(query)

def insert():
	table = input("Name of table: ")
	query = "insert into %s ("%(table)
	i = 0
	while True:
		i += 1
		column = input("Column: ")
		query += "%s"%(column)
		index = input("Add column?[y/n]: ")
		if index == "n":
			break
		query += ", " 
	query += ") values ("
	while i > 1:
		value = input("Value: ")
		query += "%s"%(value)
		query += ", "
		i -= 1
	value = input("Value: ")
	query += "%s"%(value)
	query += ");"
	sql(query)

def drop():
	print("1. Drop database","2. Drop table","0. Back",sep="\n")
	try:
		print("show_info::%s>"%(console), end="")
		index = int(input())
		match index:
			case 1:
				DB = input("Name database: ")
				sql("drop database %s;"%(DB))
			case 2:
				table = input("Name table: ")
				sql("drop table %s;"%(table))
			case 0:
				return
			case _:
				print('Unknown command. Try again')
	except ValueError as ve:
		print("Index Error (%s)"%(ve))

def create():
	print("1. Create database","2. Create table","0. Back",sep="\n")
	try:
		print("show_info::%s>"%(console), end="")
		index = int(input())
		match index:
			case 1:
				DB = input("Name of database: ")
				sql("create database %s;"%(DB))
				print("Create the database '%s' is successfull"%(DB))
			case 2:
				query = "create table if not exists "
				table = input("Name of table: ")
				query += table + " ("
				while True: 
					row = input("Name of row: ") + " "
					row += input("Type of data row: ")
					query += row
					index = input("Add row?[y/n]: ")
					if index == "n":
						break
					query += ", "
				query += ");"
				sql(query)
			case 0:
				return
			case _:
				print('Unknown command. Try again')
	except ValueError as ve:
		print("Index Error (%s)"%(ve))

def insert():
	table = input("Name of table: ")
	query = "insert into %s ("%(table)
	i = 0
	while True:
		i += 1
		column = input("Column: ")
		query += "%s"%(column)
		index = input("Add column?[y/n]: ")
		if index == "n":
			break
		query += ", " 
	query += ") values ("
	while i > 1:
		value = input("Value: ")
		query += "%s"%(value)
		query += ", "
		i -= 1
	value = input("Value: ")
	query += "%s"%(value)
	query += ");"
	sql(query)

try:
	cnx = connect(**cfg);	print("Connection to",cfg['host'],"from",cfg["user"],"is successfully.")
	console = cfg['host']+"@"+cfg["user"]
	show_menu()
	while True:
		print("main_menu::%s>"%(console), end="")
		try:
			index = int(input())
			match index:
				case 1:
					show_menu()
				case 2:
					DB = input("Name of database: ")
					if sql("use " + DB + ";"):
						new_console = console[0:26] + "@%s'"%(DB)
						console = new_console[:]
				case 3:
					show_info()
				case 4:
					select()
				case 5:
					drop()
				case 6:
					create()
				case 7:
					insert()
				case 9:
					sql()
				case 0:
					print("Exit from session. Disconnecting")
					cnx.close()
					break
				case _:
					print('Unknown command. Try again')
		except ValueError as ve:
			print("Index Error",ve)
except Error as e:
	print (e)


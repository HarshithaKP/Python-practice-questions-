# Implement a python code for the database CRUD operations.
import mysql.connector
import sys
global conn,mycursor

conn=mysql.connector.connect(host="localhost",user="root",password="root")

def connection():
	if conn.is_connected():
		print("Connected to Database ")
		return True;

	else:
		print("Unable to connect to database")
		return False;

def create_database():
	mycursor=conn.cursor()
	query="CREATE DATABASE users"
	if connection():
		mycursor.execute(query)
		print("Database created ")
	else:
		print("Unable to connect to database ")

def create_table():
	conn=mysql.connector.connect(host="localhost",user="root",password="root",database="users")
	try:
		if conn.is_connected():
			mycursor=conn.cursor()
			mycursor.execute("CREATE TABLE users181041008(id INT(10),name VARCHAR(40))")
			print("Table created")
	except Exception as e:
		print("Unable to create table")

def insertion():
	conn=mysql.connector.connect(host="localhost",user="root",password="root",database="users")
	if conn.is_connected():
		print("Connected to Database")
		query="INSERT INTO users181041008(id,name)VALUES(%s,%s)"
		i=int(input("ENter ID of user :"))
		name=input("Enter the user name :")
		args=(i,name)
		mycursor=conn.cursor()
		mycursor.execute(query,args)
		conn.commit()
		print("Successfully inserted")

	else:
		print("Unable to connect to database")
	conn.close()

def retrieve():
	conn=mysql.connector.connect(host="localhost",user="root",password="root",database="users")
	if conn.is_connected():
		query="SELECT * FROM users181041008"
		mycursor=conn.cursor()
		mycursor.execute(query)
		rows=mycursor.fetchall()
		for row in rows:
			print(row)

	else:
		print("Unable to connect to database")

	conn.close()

def delete_table():
	conn=mysql.connector.connect(host="localhost",user="root",password="root",database="users")
	if conn.is_connected():
		query="DROP TABLE users181041008"
		mycursor=conn.cursor()
		mycursor.execute(query)
		print("Table deleted ")

def main():
	while True:
		print("1: Create Database users")
		print("2: Create Table users181041008")
		print("3: Insert values")
		print("4: Display values")
		print("5: Delete Table users181041008")
		print("q: Exit ")
		option=input("Choose your option :")
		if(option=='1'):
			create_database()
		if(option=='2'):
			create_table()
		if(option=='3'):
			insertion()
		if(option=='4'):
			retrieve()
		if(option=='5'):
			delete_table()
		if(option=='q'):
			sys.exit()

if __name__ == '__main__':
	main()








	









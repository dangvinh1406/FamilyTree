import sqlite3
import os

class DatabaseManager:
	def __init__(self):
		# if not os.path.isfile(db):

		self.__connection = sqlite3.connect('dbft.db')
		self.__connection.execute(
			"""
			CREATE TABLE IF NOT EXISTS family(
				family_id INTEGER PRIMARY KEY AUTOINCREMENT,
				family_name TEXT NOT NULL
			);
			"""
		)
		self.__connection.execute(
			"""
			CREATE TABLE IF NOT EXISTS person(
				person_id INTEGER PRIMARY KEY AUTOINCREMENT,
				family_id INT,
				person_name TEXT NOT NULL,
				birth_year INT NOT NULL,
				gender INT NOT NULL,
				FOREIGN KEY(family_id) REFERENCES family(family_id)
			);
			"""
		)

	def getCurrentId(self, tablename="family"):
		if tablename not in ["person", "family"]:
			return -1
		cursor = self.__connection.cursor()
		cursor.execute(
			"SELECT last_insert_rowid();"
		)
		return cursor.fetchone()[0]

	def storeFamily(self, name):
		cursor = self.__connection.cursor()
		cursor.execute(
			"INSERT INTO family(family_name) VALUES("+"'"+name+"');"
		)

		cursor.execute(
			"SELECT * FROM family;"
		)
		print(cursor.fetchall())

	def storePerson(self, family, name, year, gender):
		cursor = self.__connection.cursor()
		cursor.execute(
			"INSERT INTO person(family_id, person_name, birth_year,gender)"+ \
			"VALUES("+str(family)+","+"'"+name+"',"+str(year)+","+str(gender)+");"
		)

		cursor.execute(
			"SELECT * FROM person;"
		)
		print(cursor.fetchall())

	def commit(self):
		self.__connection.commit()

	def abort(self):
		self.__connection.close()
		self.__connection = sqlite3.connect('dbft.db')

		
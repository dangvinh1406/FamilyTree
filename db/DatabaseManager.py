import sqlite3
import os

class DatabaseManager:
	def __init__(self, dataFile="data.fam", isInit=True):
		self.__connection = sqlite3.connect(dataFile)
		if isInit:
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
					father_id INT NOT NULL,
					mother_id INT NOT NULL,
					FOREIGN KEY(family_id) REFERENCES family(family_id)
				);
				"""
			)
			self.__connection.execute(
				"""
				CREATE TABLE IF NOT EXISTS couple(
					husband_id INT NOT NULL,
					wife_id INT NOT NULL,
					FOREIGN KEY(husband_id) REFERENCES person(person_id),
					FOREIGN KEY(wife_id) REFERENCES person(person_id)
				);
				"""
			)

	def getCurrentId(self):
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

	def storePerson(self, family, name, year, gender, father, mother):
		cursor = self.__connection.cursor()
		cursor.execute(
			"INSERT INTO person(family_id,person_name,birth_year,gender,father_id,mother_id)"+ \
			"VALUES("+str(family)+","+ \
			"'"+name+"',"+ \
			str(year)+","+ \
			str(gender)+","+ \
			str(father)+","+ \
			str(mother)+");"
		)

		cursor.execute(
			"SELECT * FROM person;"
		)
		print(cursor.fetchall())

	def storeCouple(self, husband, wife):
		cursor = self.__connection.cursor()
		cursor.execute(
			"INSERT INTO couple(husband_id,wife_id)"+ \
			"VALUES("+str(husband)+","+str(wife)+");"
		)

		cursor.execute(
			"SELECT * FROM couple;"
		)
		print(cursor.fetchall())

	def commit(self):
		self.__connection.commit()

	def abort(self):
		self.__connection.close()
		self.__connection = sqlite3.connect('dbft.db')

		
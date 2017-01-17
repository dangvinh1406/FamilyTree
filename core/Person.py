
class GENDER:
	MALE = 0
	FEMALE = 1

class Person:
	def __init__(self, idp, name, gender, year):
		self.__id = idp
		self.__fullName = name
		self.__gender = gender
		self.__birthYear = year
		self.__father = None
		self.__mother = None
		self.__child = []

	def getID(self):
		return self.__id

	def getBirthYear(self):
		return self.__birthYear

	def setMother(self, motherId):
		self.__mother = motherId

	def setFather(self, fatherId):
		self.__father = fatherId

	def addChildren(self, childrenId):
		self.__child.append(childrenId)


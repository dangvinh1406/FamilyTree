import math as ma

class GENDER:
	MALE = -1
	FEMALE = 1

	@staticmethod
	def toString(gender):
		if gender == GENDER.MALE:
			return "male"
		elif gender == GENDER.FEMALE:
			return "female"
		else:
			return "unknown"

	@staticmethod
	def fromString(gender):
		if gender == "male" or gender == "MALE":
			return GENDER.MALE
		else:
			return GENDER.FEMALE

	@staticmethod
	def fromInt(gender):
		if gender == 1:
			return GENDER.FEMALE
		else:
			return GENDER.MALE

class RELATIONSHIP:
	IS_WIFE = 0
	IS_HUSBAND = 1
	IS_CHILDREN = 2
	IS_MOTHER = 3
	IS_FATHER = 4

class Person:
	def __init__(self, idp, name, year, gender):
		self.__id = idp
		self.__fullName = name
		self.__gender = gender
		self.__birthYear = year
		self.__fatherId = None
		self.__motherId = None
		self.__coupleIds = []
		self.__childIds = []

	def setMother(self, mother):
		if mother.getGender() == GENDER.FEMALE and \
		mother.getBirthYear() > self.__birthYear+10 and \
		mother.getBirthYear() < self.__birthYear+60:
			self.__motherId = mother.getID()
			mother.addChildren(self)
		else:
			print("Error: [Person] Can not set "+mother.getName()+ \
				" as mother of "+self.__fullName)

	def setFather(self, father):
		if mother.getGender() == GENDER.FEMALE and \
		mother.getBirthYear() > self.__birthYear+10 and \
		mother.getBirthYear() < self.__birthYear+60:
			self.__fatherId = father.getID()
			father.addChildren(self)
		else:
			print("Error: [Person] Can not set "+father.getName()+ \
				" as father of "+self.__fullName)

	def addCouple(self, couple):
		if couple.getGender()+self.__gender == 0 and \
		ma.fabs(mother.getBirthYear()-self.__birthYear) < 60:
			self.__coupleIds.append(couple.getID())
			couple.addCouple(self)
		else:
			print("Error: [Person] Can not add "+couple.getName()+ \
				" as a couple of "+self.__fullName)

	def addChildren(self, children):
		if children.getBirthYear()+10 < self.__birthYear and \
		children.getBirthYear()+60 > self.__birthYear:
			self.__childIds.append(children.getID())
			if self.__gender == GENDER.MALE:
				children.setFather(self)
			else:
				children.setMother(self)
		else:
			print("Error: [Person] Can not add "+children.getName()+ \
				" as a children of "+self.__fullName)

	def getID(self):
		return self.__id

	def getName(self):
		return self.__fullName

	def getGender(self):
		return self.__gender

	def getBirthYear(self):
		return self.__birthYear

	def getFatherID(self):
		return self.__fatherId

	def getMotherID(self):
		return self.__motherId

	def getCoupleIDs(self):
		return self.__coupleIds

	def getChildIDs(self):
		return self.__childIds

	def getNumOfChilds(self):
		return len(self.__childIds)

	def toString(self):
		return str(self.getID())+". "+ \
				self.getName()+" ("+ \
				str(getBirthYear(self))+"), "+ \
				GENDER.toString(self.getGender())


	





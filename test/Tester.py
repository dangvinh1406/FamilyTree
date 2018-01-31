import sys
import os
sys.path.insert(0, os.path.abspath(os.getcwd()+"../../"))

from core.FamilyTree import *
from core.Person import *

RELATIONSHIP_NAME = {
	RELATIONSHIP.IS_NULL: " [is the current person] ",
	RELATIONSHIP.IS_WIFE: " [is the wife of] ",
	RELATIONSHIP.IS_HUSBAND: " [is the husband of] ",
	RELATIONSHIP.IS_CHILDREN: " [is the children of] ",
	RELATIONSHIP.IS_MOTHER: " [is the mother of] ",
	RELATIONSHIP.IS_FATHER: " [is the father of] "
}

if __name__ == '__main__':
	family = FamilyTree(1, "gia dinh toi")

	family.addPerson(1, "toi", 1994, GENDER.MALE)
	family.addPerson(2, "vo toi", 1994, GENDER.FEMALE)
	family.setCouple(1, 2)

	family.addPerson(3, "cha toi", 1954, GENDER.MALE)
	family.addPerson(4, "me toi", 1955, GENDER.FEMALE)
	family.setCouple(3, 4)
	family.setFather(3, 1)
	family.setMother(4, 1)

	family.addPerson(5, "anh trai toi", 1990, GENDER.MALE)
	family.addPerson(6, "vo anh trai toi", 1990, GENDER.FEMALE)
	family.setCouple(5, 6)
	family.setFather(3, 5)
	family.setMother(4, 5)

	family.addPerson(7, "ong noi toi", 1920, GENDER.MALE)
	family.addPerson(8, "ba noi toi", 1925, GENDER.FEMALE)
	family.setCouple(7, 8)
	family.setFather(7, 3)
	family.setMother(8, 3)

	family.addPerson(9, "chi cua cha toi", 1950, GENDER.FEMALE)
	family.addPerson(10, "chong cua chi cha toi", 1950, GENDER.MALE)
	family.setCouple(9, 10)
	family.setFather(7, 9)
	family.setMother(8, 9)

	family.addPerson(11, "em cua cha toi", 1950, GENDER.MALE)
	family.setFather(7, 11)
	family.setMother(8, 11)

	family.addPerson(12, "con cua chi cha toi", 1990, GENDER.FEMALE)
	family.addPerson(13, "con cua chi cha toi", 1989, GENDER.MALE)
	family.setFather(10, 12)
	family.setMother(9, 12)
	family.setFather(10, 13)
	family.setMother(9, 13)

	family.addPerson(14, "con cua anh trai toi", 2010, GENDER.MALE)
	family.setFather(5, 14)
	family.setMother(6, 14)

	family.addPerson(15, "cha cua ong noi toi", 1880, GENDER.MALE)
	family.addPerson(16, "me cua ong noi toi", 1885, GENDER.FEMALE)
	family.setCouple(15, 16)
	family.setFather(15, 7)
	family.setMother(16, 7)

	family.addPerson(17, "anh trai ong noi toi", 1916, GENDER.MALE)
	family.setFather(15, 17)
	family.setMother(16, 17)

	print(family.toString())

	relationships = family.search(17, 10)

	for relationship in relationships:
		print("--------------")
		for i in range(len(relationship)):
			string = family.lookupPerson(relationship[i][0]).toString() \
				+RELATIONSHIP_NAME[relationship[i][1]]
			if i > 0:
				string += family.lookupPerson(relationship[i-1][0]).toString()
			print(string)





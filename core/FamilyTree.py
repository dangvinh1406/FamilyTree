from core.Person import *
import copy

class FamilyTree:
	def __init__(self, idf, familyName):
		self.__idFamily = idf
		self.__familyName = familyName
		self.__tree = {}

	def lookupPerson(self, idp):
		return copy.deepcopy(self.__tree[idp])

	def addPerson(self, idp, name, year, gender):
		person = Person(idp, name, year, gender)
		self.__tree[person.getID()] = person

	def setFather(self, fatherId, childrenId):
		if fatherId <= 0:
			return
		self.__tree[childrenId].setFather(self.__tree[fatherId])

	def setMother(self, motherId, childrenId):
		if motherId <= 0:
			return
		self.__tree[childrenId].setMother(self.__tree[motherId])

	def setCouple(self, person1Id, person2Id):
		if person1Id <= 0:
			return
		self.__tree[person2Id].setCouple(self.__tree[person1Id])

	def search(self, rootId, leafId):
		if rootId not in self.__tree or leafId not in self.__tree:
			print("Error: [FamilyTree] Person is not in family")
			return

		# perform BFS to find the relationship with 2 persons
		relationships = []
		backTracer = {}
		Q = [rootId]
		history = []
		while len(Q) > 0:
			nodeId = Q.pop()
			history.append(nodeId)

			# current person is the interested person
			if nodeId == leafId:
				# trace back to find a relationship path, continue to search another path
				p = backTracer[leafId]
				relationship = [(leafId, RELATIONSHIP.IS_NULL), p]
				while p[0] != rootId:
					p = backTracer[p[0]]
					relationship.append(p)
				relationships.append(relationship)

			# search in his/her couples
			for coupleID in self.__tree[nodeId].getCoupleIDs():
				if coupleID not in history and coupleID is not None:
					Q.append(coupleID)
					if self.__tree[nodeId].getGender() == GENDER.MALE:
						backTracer[coupleID] = (nodeId, RELATIONSHIP.IS_HUSBAND)
					else:
						backTracer[coupleID] = (nodeId, RELATIONSHIP.IS_WIFE)

			# search in his/her children
			for childrenID in self.__tree[nodeId].getChildIDs():
				if childrenID not in history and childrenID is not None:
					Q.append(childrenID)
					if self.__tree[nodeId].getGender() == GENDER.MALE:
						backTracer[childrenID] = (nodeId, RELATIONSHIP.IS_FATHER)
					else:
						backTracer[childrenID] = (nodeId, RELATIONSHIP.IS_MOTHER)

			# search in his/her father
			fatherID = self.__tree[nodeId].getFatherID()
			if fatherID not in history and fatherID is not None:
				Q.append(fatherID)
				backTracer[self.__tree[nodeId].getFatherID()] = (nodeId, RELATIONSHIP.IS_CHILDREN)

		return relationships

	def toString(self):
		stringData = ""
		for key, person in self.__tree.items():
			stringData += person.toString()+"\n"
		return stringData

	def toListString(self, omitGender=0):
		listData = []
		for key, person in self.__tree.iteritems():
			if person.getGender() != omitGender:
				listData.append(person.toString()+"\n")
		if len(listData) == 0:
			listData.append("no person to choose")
		return listData

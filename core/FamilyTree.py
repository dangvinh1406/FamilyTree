import Queue as qu

from core.Person import *

class FamilyTree:
	def __init__(self, idf, familyName):
		self.__idFamily = idf
		self.__familyName = familyName
		self.__tree = {}
		self.__backTracer = {}

	def addPerson(self, person):
		self.__tree[person.getID()] = person
		self.__backTracer[person.getID()] = -1

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
		if personId1 not in self.__tree or personId2 not in self.__tree:
			print("Error: [FamilyTree] Person is not in family")
			return

		# perform BFS to find the relationship with 2 persons
		relationships = []
		Q = qu.Queue()
		Q.put(rootId)
		history = []
		while not Q.empty():
			nodeId = Q.get()
			history.append(nodeId)

			# current person is the interested person
			if nodeId == leafId:
				# trace back to find a relationship path, continue to search another path
				p = self.__backTracer[leafId]
				relationship = [p]
				while p[0] != rootId:
					p = self.__backTracer[p[0]]
					relationship.append(p)
				relationships.append(relationship)

			# search in his/her couples
			for coupleID in self.__tree[nodeId].getCoupleIDs():
				if coupleID not in history:
					Q.put(coupleID)
					if self.__tree[nodeId].getGender == GENDER.MALE:
						self.__backTracer[coupleID] = (nodeId, RELATIONSHIP.HUSBAND)
					else:
						self.__backTracer[coupleID] = (nodeId, RELATIONSHIP.WIFE)

			# search in his/her children
			for childrenID in self.__tree[nodeId].getChildIDs():
				if childrenID not in history:
					Q.put(childrenID)
					if self.__tree[nodeId].getGender == GENDER.MALE:
						self.__backTracer[childrenID] = (nodeId, RELATIONSHIP.FATHER)
					else:
						self.__backTracer[childrenID] = (nodeId, RELATIONSHIP.MOTHER)

			# search in his/her father
			if self.__tree[nodeId].getFatherID() not in history:
				Q.put(self.__tree[nodeId].getFatherID())
				self.__backTracer[self.__tree[nodeId].getFatherID()] = (nodeId, RELATIONSHIP.CHILDREN)

		return relationships

	def toString(self):
		stringData = ""
		for key, person in self.__tree.iteritems():
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
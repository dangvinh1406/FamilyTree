import queue as qu

from core.Person import *

class FamilyTree:
	def __init__(self, familyId):
		self.__familyID = familyId
		self.__tree = {}
		self.__backTracer = {}

	def addPerson(self, person):
		self.__tree[person.getID()] = person
		self.__backTracer[person.getID()] = "none"

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
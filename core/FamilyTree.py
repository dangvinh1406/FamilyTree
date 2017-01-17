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

	def search(self, personId1, personId2):
		if personId1 not in self.__tree or personId2 not in self.__tree:
			print("Error: [FamilyTree] Person is not in family")
			return
		rootId = personId1
		leafId = personId2
		if self.__tree[personId1].getBirthYear > self.__tree[personId2].getBirthYear:
			rootId = personId2
			leafId = personId1

		# perform BFS to find the relationship with 2 persons
		Q = qu.Queue()
		Q.put(rootId)
		while not Q.empty():
			nodeId = Q.get()

			# current person is the interested person
			if nodeId == leafId:
				# find a relationship path, continue to search another path
				pass

			# search in his/her couples
			for coupleID in self.__tree[nodeId].getCoupleIDs():
				Q.put(coupleID)

			# search in his/her siblings


			# search in his/her children
			for childrenID in self.__tree[nodeId].getChildIDs():
				if childrenID not in Q:
					Q.put(childrenID)
			
			# search in his/her father ???
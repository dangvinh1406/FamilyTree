from core.Person import *

class FamilyTree:
	def __init__(self):
		self.__tree = {}

	def addPerson(self, person):
		self.__tree[person.getID()] = person

	def search(self, personId1, personId2):
		if personId1 not in self.__tree or personId2 not in self.__tree:
			print("Error: [FamilyTree] Person is not in family")
			return
		root = personId1
		leaf = personId2
		if self.__tree[personId1].getBirthYear > self.__tree[personId2].getBirthYear:
			root = personId2
			leaf = personId1
		# perform BFS to find the relationship with 2 persons
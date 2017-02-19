

class Utils:
	@staticmethod
	def cropIndex(aString):
		cropString = ""
		for ch in aString:
			if ch == ".":
				break
			cropString += ch
		try:
			return int(cropString)
		except:
			return -1
import random


class Rlist:
	def __init__(self, list: list, notList: list = []):
		self.list = list
		self.notList = notList
		self.outputList = []
		for i in self.list:
			if i not in self.notList:
				self.outputList.append(i)
		self.output = self.outputList[random.randint(0, len(self.outputList) - 1)]

	def __str__(self):
		return str(self.output)

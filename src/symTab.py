# class symTabEntry(self):
# 	"""symTabEntry data structure"""
# 	def __init__(self, name):
# 		self.name = name
# 		self.size = -1
# 		self.type = undefined
			


class SymTable:
	"""Symbol Table data structure"""
	def __init__(self):
		self.EntryList = {'Integer':'typedef','Char':'typedef','String':'typedef'}
		self.num_entries = 0


	def add_id(self,name):
		self.EntryList[name] = {}
		self.num_entries += 1
		self.EntryList[name]['name'] = name
		return self.EntryList[name]

	def look_up(self,name):
		if name in self.EntryList:
			return self.EntryList[name]
		else:
			return None


		
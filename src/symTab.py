# class symTabEntry(self):
# 	"""symTabEntry data structure"""
# 	def __init__(self, name):
# 		self.name = name
# 		self.size = -1
# 		self.type = undefined
class Scope:
	def __init__(self,parent):
		self.EntryList = {'Integer':'typedef','Char':'typedef','String':'typedef'}
		self.num_entries = 0
		self.parentScope = parent


	def add_id(self,name):
		self.EntryList[name] = {}
		self.num_entries += 1
		self.EntryList[name]['name'] = name
		return self.EntryList[name]

	def look_up(self,name):
		scope = self
		while(scope is not None):
			if name in scope.EntryList:
				return scope.EntryList[name]
			else:
				scope = scope.parentScope
		return None

	def update_id(self,name,id_dict):
		req_id_dict = self.look_up(name=name)
		if req_id_dict is None:
			print "Can't update since such an identifier didn't exist"
		else:
			for id_key in id_dict:
				req_id_dict[id_key] = id_dict[id_key]

				
						


class SymTable:
	"""Symbol Table data structure"""
	def __init__(self):
		self.currentScope = Scope(parent=None)

	def begin_scope(self):
		self.currentScope = Scope(parent=self.currentScope)

	def end_scope(self):
		self.currentScope = self.currentScope.parentScope



		
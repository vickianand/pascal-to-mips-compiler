# class symTabEntry(self):
# 	"""symTabEntry data structure"""
# 	def __init__(self, name):
# 		self.name = name
# 		self.size = -1
# 		self.type = undefined
class Scope:
	def __init__(self,parent,name):
		self.EntryList = {'integer':{'type':'typedef', 'width': 4},
							'real':{'type':'typedef', 'width': 4},
							'char':{'type':'typedef', 'width': 1},
							'string':{'type':'typedef', 'width': 4}
						} # include boolean, long , float etc.
		self.num_entries = 0
		self.parentScope = parent
		self.name = name


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
		self.currentScope = Scope(parent=None,name='root')
		self.temp_var_count = 0;
		self.label_count = 0;

	def begin_scope(self,name):
		self.currentScope = Scope(parent=self.currentScope,name=name)

	def end_scope(self):
		self.currentScope = self.currentScope.parentScope

	def new_temp(self):
		self.temp_var_count += 1
		return "t" + str(self.temp_var_count)

	def new_label(self):
		self.label_count += 1
		return "label_" + str(self.label_count)



		
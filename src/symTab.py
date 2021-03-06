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
							'char':{'type':'typedef', 'width': 4},
							'string':{'type':'typedef', 'width': 4}
						} # include boolean, long , float etc.
		self.tempList = {}
		self.width = 0
		self.num_entries = 0
		self.parentScope = parent
		self.name = name


	def add_id(self,name):
		self.EntryList[name] = {}
		self.num_entries += 1
		self.EntryList[name]['name'] = name
		return self.EntryList[name]

	def add_temp(self,name,typ,width,corres_identifier,s_entry,arr_access):
		self.tempList[name] = {'offset':self.width,'width':width,'type':typ,'corres_identifier':corres_identifier,'s_entry':s_entry,'array_access':arr_access}
		self.width += width
		self.tempList[name]['name'] = name
		return self.tempList[name]

	# def update_temp_offset(self,name,offset):
	# 	self.tempList[name]['offset'] = offset

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
		self.scope_list = {'root':self.currentScope}

	def begin_scope(self,name):
		self.currentScope = Scope(parent=self.currentScope,name=name)
		self.scope_list[name] = self.currentScope

	def end_scope(self):
		self.currentScope = self.currentScope.parentScope

	def new_temp(self,s_entry={},typ='',width=4,name='',array_access=False):
		self.temp_var_count += 1
		name2 = "t" + str(self.temp_var_count)
		self.currentScope.add_temp(name2,typ,width,name,s_entry,array_access)
		return name2

	# def update_offset(self,name,offset):
	# 	self.currentScope.update_temp_offset(name,offset)

	# def get_offset(self,name):
	# 	return self.currentScope.tempList[name]['offset']

	def new_label(self):
		self.label_count += 1
		return "label_" + str(self.label_count)

	def print_temp(self):
		for sc_name in self.scope_list:
			print(sc_name)
			print(self.scope_list[sc_name].tempList)

	def get_func_entrylist(self,scope):
		if scope.name != 'root':
			parent = scope.parentScope
			return parent.EntryList[scope.name]
		else :
			return None



		
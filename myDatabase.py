#database
#class
#dump
#load
#selfcreate
#check if exist

import json
import os

def load(filename='table.db'):
	mydata=myDatabase(filename)
	mydata.if_exists()
	return mydata

class myDatabase:
	jobject={}

	def __init__(self,filename):
		self.filename=filename

	#action or functionality
	def dump(self):
		with open(self.filename,'w') as content:
			data = json.dumps(self.jobject)
			content.write(data)
			content.close()
		return True

	def load_file(self):
		with open(self.filename) as content:
			data=content.read()
			self.jobject=json.loads(data)
		return(self.jobject)

	def auto_dump(self):
		if self.auto_dump:
			self.dump()

	def if_exists(self):
		if os.path.exists(self.filename):
			self.load_file()
		else:
			self.dump()
			self.load_file()

	def set(self,key,value):
		dic = self.load_file()
		dic[key]=value
		self.auto_dump()
		return True

	def get(self,key):
		dic = self.load_file()
		return dic[key]

	def get_all(self):
		dic = self.load_file()
		return dic.keys()

	def get_all_value(self):
		dic = self.load_file()
		return dic.values()

	def rem(self,key):
		dic = self.load_file()
		del dic[key]
		self.auto_dump()
		return True

	def exists(self,key):
		dic = self.load_file()
		if key in dic:
			return True
		else:
			return False

	def total_keys(self):
		dic = self.load_file()
		return len(dic)

	def del_db(self):
		dic = self.load_file()
		dic.clear()
		self.auto_dump()
		return True

	def random_insert(self,number):
		def ran():
			import random
			return random.randint(1,100)
		dic = self.load_file()
		i=0
		while i<number:
			key=ran()
			if key not in dic:
				dic[key]=ran()
				i+=1
		self.auto_dump()
		return True

	def demerge(self,others):
		dic= self.load_file()
		new_object = myDatabase(others)
		a= new_object.load_file()

		dic.update(a)
		self.auto_dump()
		return True
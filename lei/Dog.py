class DogYt(object):
	_a = None
	def __init__(self,name):
		self.name = name
	def __new__(cls,name):
		if cls._a == None:
			cls._a = object.__new__(cls)	
		return cls._a
a = DogYt("zhang")	
b = DogYt("han")
print(a.name)
print(b.name)


class Xuesheng(object):
	def __init__(self,name,age,chengji):
		self.name = name
		self.age = age
		self.chengji = chengji
	def get_name(self):
		return self.name
	def get_age(self):
		return self.age
	def get_chengji(self):
		return max(self.chengji)
mz=Xuesheng("老尹",20,[85,76,99])
print(mz.get_name())
print(mz.get_age())
print(mz.get_chengji())












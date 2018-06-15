class Father(object):
	def __init__(self,name):
		self.name = name
	def kaiche(self):
		print("是个老司机......")
	def eat(self):
		print("能吃")
class Son(Father):
	def __init__(self,name):
#		Father.__init__(self,name)
		super().__init__(name)
	def kaiche(self):
#		print("是个赛车手......")
		super().kaiche()
son = Son("小王")
print(son.name)
son.kaiche()
#erzi.kaiche()

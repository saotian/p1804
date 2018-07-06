class People(object):
	def __init__(self,name,height,weight):
		self.name = name
		self.height = height
		self.weight = weight
	def introduce(self):
		print("我的名字是%s,身高%s,体重%s"%(self.name,self.height,self.weight))


huahua = People("花花",180,130)
huahua.introduce()

caocao = People("草草",185,120)
caocao.introduce()




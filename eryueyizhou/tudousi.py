class Potato:
	def __init__(self):
		self.info = "刚取出的土豆"
		self.lever = 0
		self.list1 = []
	def cook(self,a):
		self.lever += a
		if self.lever >= 10:
			self.info = "炒糊了"
		elif self.lever >=8:
			self.info = "火大了"
		elif self.lever == 6:
			self.info = "可口的土豆丝"
		elif self.lever >=4 :
			self.info = "僵硬的土豆丝"
		else:
			self.info = "生的土豆丝"
	def taste(self,seasoning):
		self.list1.append(seasoning)
	def __str__(self):
		for i in self.list1:
			self.info += i + ","
		self.info = self.info.strip(",")
		return "土豆是:%s,炒土豆一共用了%d分钟"%(self.info, self.lever)	




td1 = Potato()
print(td1.info)
td1.cook(2)
print(td1.info)
td1.cook(4)
print(td1.info)
td1.taste("孜然")
td1.taste("香辣")
td1.taste("酸甜")
print(td1)


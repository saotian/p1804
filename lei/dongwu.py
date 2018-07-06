class dongwu():
	def __init__(self,name):
		self.name = name
	def run(self):
		print("正在奔跑")
class Dog(dongwu):
	pass
	def aname(self):
		print("他的名字是%s"%self.name)

kk=Dog("zhangsan")
kk.aname()
kk.run()










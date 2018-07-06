class Cat():
	def eat(self):
		print("吃猫粮")
	def drink(self):
		print("喝牛奶")
	def introduce(self):
		print("我叫%s,是一只%s的猫，今年%d岁" % (self.name,self.color,self.sex))

huahua = Cat()
huahua.eat()
huahua.drink()
huahua.name = "花花"
huahua.color = '白色'
huahua.sex = 2
huahua.introduce()


erha = Cat()
erha.name = "晓晓"
erha.color = "花色"
erha.sex = 3
erha.introduce()






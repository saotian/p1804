class Dog(object):
	def wan(self):
		return "普通小狗玩泥巴"
class xiaotianquan(Dog):
	def wan(self):
		return "哮天犬在天上玩泥巴"
class People(object):
	def play_with(self,dog): 
		print("人在和",dog.wan())

a = Dog()
xtq = xiaotianquan()
b = People()
b.play_with(a)
b.play_with(xtq)


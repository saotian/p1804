class Donkey(object):  #驴类　　多继承
	def manzou(self):
		print("走路慢......")
class Horse(object):   #马类
	def naili(self):
		print("耐力强......")	
class Mule(Donkey,Horse):   #继承者　　骡子
	pass
骡子 = Mule()
骡子.manzou()
骡子.naili()





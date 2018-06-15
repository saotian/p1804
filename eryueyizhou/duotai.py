class Duck(object):
	def walk(self):
		print("鸭子在走路")
	def swim(self):
		print("鸭子在游泳")
class People(object):
	def walk(self):
		print("老王在走路")
	def swim(self):
		print("老王在游泳")

def Func(obj):
	obj.walk()
	obj.swim()



duck = Duck()
ren = People()

Func(duck)
Func(ren)

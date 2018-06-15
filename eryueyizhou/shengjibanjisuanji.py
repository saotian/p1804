class Calc(object):
	__instance = None
	__flag = True
	def __init__(self,name):
		if Calc.__flag == True:
			self.name = name
			Calc.__flag = False
	def __new__(cls,*args):
		if cls.__instance is None:
			cls.__instance = object.__new__(cls)
		return cls.__instance
	def add(self,a,b):
		return a+b
	def minus(self,a,b):
		return a-b
	def mul(self,a,b):
		return a*b
	def div(self,a,b):
		return a/b

class SimpleCalc(Calc):
	def ji_suna(self,x,y,symbol):
		if symbol == "+":
			return super().add(x,y)
		elif symbol == "-":
			return super().minus(x,y)
		elif symbol == "*":
			return super().mul(x,y)
		elif symbol == "/":
			return super().div(x,y)
		else:
			return "输入有误"
c1 = SimpleCalc("计算机")
try:
	r = c1.ji_suan(20, 2 , "*")
	print(r)
except Exception as rr:
	print("计算出现错误：%s"%rr)


















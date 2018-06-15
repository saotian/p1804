class Jisuanji(object):
	__shifo = None
	def __new__(cls,*n):
		if cls.__shifo == None:
			cls.__shifo = super().__new__(cls)
		return cls.__shifo
	def jisuan(self):
		a = int(input("请输入一个数字:"))
		while True:	
			b = input("请输入计算符号:")
			c = int(input("请在输入一个数字"))
			if b == "+":
				o = a+c
				print(o)
			elif b == "-":
				o = a-c
				print(o)
			elif b == "*":
				o = a*c 
				print(o)
			elif b == "/":
				o =	a/c
				print(o)
			a = o
try:
	jsj = Jisuanji()
	jsj.jisuan()
except Exception as r:
	print("异常是%s"%r)






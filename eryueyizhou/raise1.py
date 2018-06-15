class Test(object):
	def __init__(self):
		self.switch = "open"
	def div(self,a,b):
		try:
			return a/b
		except Exception as er:
			if self.switch == "open":
				print("出现了异常：%s"%er)
			else:
				raise
t = Test()
t.switch = "open"
t.div(2,1)


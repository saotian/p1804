class Mrerror(Exception):
	def __init__(self,str_error)
		self.name = str_error

	def get_pwd():
		pwd = input("请输入密码")
		if len(pwd) < 6:
		raise Myerror("密码小于６位")
try:
	get_pwd()
except Exception as er:
	print ("异常%s"%er)











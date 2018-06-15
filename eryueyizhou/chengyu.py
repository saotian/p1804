class Chengyu(object):
	__girl = None
	__only_you = False
	def __init__(self,name):
		if self.__only_you == False:
			self.name = name
			self.__only_you = True
	def __new__(cls,*args):
		if cls.__girl == None:
			cls.__girl = object.__new__(cls)
		return cls.__girl


gir1 = Chengyu("程宇")
print(gir1.name)
gir2 = Chengyu("猪")
print(gir2.name)












class Car(object):
	__instace = None
	__init_flag = True
	def __init__(self,name):
		if Car.__init_flag == True:
			self.name = name
			Car.__init_flag = False
	def __new__(cls,*k):
		if cls.__instace == None:
			cls.__instace = object.__new__(cls)
		return cls.__instace

c = Car("宝马")
print(c.name)
c1 = Car("奔驰")
print(c1.name)
c2 = Car("玛莎拉蒂")
print(c2.name)


print(id(c))
print(id(c1))
print(id(c2))

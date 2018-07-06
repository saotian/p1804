class PeopleYt(object):
	def __init__(self):
		self.__money = 0
	def getmoney(self):
		return self.__money 
	def setmoney(self,value):
		self.__money = value
	a = property(getmoney,setmoney)
class zhangsan(PeopleYt):
	def __init__(self):
		PeopleYt.__init__(self)
zs=zhangsan()
print(zs.a)
zs.a = 1000
print(zs.a)





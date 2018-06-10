class People:
	def __init__(self,name,salary):
		self.__name = name
		self.salary = salary
	def get_name(self):
		return self.__name
	def get_salary(self):
		return self.salary
	def set_name(self,n):
		self.name = n
		return self.name
	def __str__(self):
		return self.__name
laowang = People("老王",100000)
print(laowang.get_name())
print(laowang.get_salary())






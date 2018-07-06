class PeopleYt:
	def __init__(self,name,money):
		self.name = name
		self.__money = money
	def get_name(self):
		return self.name
	def get_money(self):
		return self.__money
	def set_money(self):
		return self.__money
	def __str__(self):
		return self.__money
class zhangsan(PeopleYt):
	pass

zh = PeopleYt("zhangsan",100000)
print(zhangsan.get_name())
print(zhangsan.get_money())





class People1(object):
	def __init__(self):
		self.__money = 0
	@property
	def money(self):
		return self.__money
	@money.setter
	def money(self,value):
		self.__money = value
#	money = property(get_money,set_money)

p = People1()
print(p.money)
#p.money = 99111
#print(p.money)

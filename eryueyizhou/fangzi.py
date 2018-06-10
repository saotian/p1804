class House:
	def __init__(self, area, addr):
		self.area = area
		self.addr = addr
		self.items = []
	def __str__(self):
		return "房子大小是%s,地址位于：%s,其中包含的家具有：%s"%(self.area,self.addr,self.items)

	



	def add_items(self,item):
		if int(self.area) > int(item.area):
			self.area -= self.area
			self.items.append(item.name)


class Bed:
	def __init__(self,area,name):
		self.area = area
		self.name = name
	def __str__(self):
		return "%s已经购买，他的大小是%s"%(self.name,self.area)


fz = House(200,"天安门前门1号")
print(fz)
baby_bed = Bed(100,"婴儿床")
print(baby_bed)
fz.add_items(baby_bed)
print(fz)







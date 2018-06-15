class Qiche(object):
	def __init__(self,name):
		self.name = name
class Dazhong(Qiche):	
	def pao(self):
		return "大众在公路上飞驰"
class Baoma(Qiche):
	def pao(self):
		return "宝马在公路上飞驰"
class Benchi(Qiche):
	def pao(self):
		return "奔驰在公路上飞驰"
		
class People(object):
	def __init__(self,name):
		self.name = name

	def kaiche(self,che):
		print("%s开着%s" %(self.name,che.pao()))

qi = Qiche("大奔")
dz = Dazhong("大众")
bm = Baoma("宝马")
bc = Benchi("奔驰")
ren = People("老王")
ren.kaiche(bm)
ren.kaiche(dz)
ren.kaiche(bc)




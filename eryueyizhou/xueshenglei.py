class student:
	def __init__(self, name, sex, age):
		self.name = name
		self.sex = sex
		self.age = age
		self.chengji_1 = {}
	def add_tianjia(self,k,v):
		self.chengji_1[k] = v
	def __str__(self):
		return "名字:"+self.name+"年龄:"+self.sex+"性别:"+self.age+"成绩"+self.chengji
	def chengji(self):
		for i in range(1,4):
			k = int(input("请输入学生姓名:"))
			v = int(input("请输入学生成绩:"))
			self.add_tianjia(k,v)

xiao = student("小明","男","19")
xiao.chengji()
print(xiao)



























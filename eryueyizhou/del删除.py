class Animal:
	def __init__(self,name):
		self.name = name
		self.f = open("namee.txt","w")
	def get_name(self):
		pass-
	def __del__(self):
		print("________销毁________")
dog = Animal("大黄")
dog1 = dog
print("==============")





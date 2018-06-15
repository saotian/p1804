class People(object):
	guoji = "china"
	def __init__(eslf):
		self.name = "小明"
	def get_name(self):
		return self.name
	@classmethod
	def get_guoji(cls):
		return cls.guoji
	def say_chinese(self):
		print("中国话")
xiaoming = People()
print(People.guoji)
print(People.get-guoji)
People.say_chinese()


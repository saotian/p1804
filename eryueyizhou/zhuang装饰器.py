def wai(x):
	def nei(name='员工'):
		if name == '员工':
			x()
		else:
			print("只能本公司的人能查看")
	return nei


@wai
def f1():
	print("f1")
def f2():
	print("f2")
def f3():
	print("f3")
def f4():
	print("f4")

f1()
f2()

'''
while True:
	a = input("请输入你要查看的内容：")
	if a == "f1":
		wai(f1)("员工")
	elif a == "f2":
		wai(f2)("员工")
	elif a == "f3":
		wai(f3)("员工")
	elif a == "f4":
		wai(f4)("员工")
	else:
		print("退出")
		break
'''

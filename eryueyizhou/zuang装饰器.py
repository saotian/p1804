#有参装饰器
def w1(fun):
	def w2(a,b):
		print ("a=%d,b=%d"%(a,b))
		print("函数调用千的检查")
		fun(a,b)
	return w2
@w1
def foo(c,d):
	print("sotou")
	print("sotou 参数是%d%d"%(c,d))

foo(5,6)







def w1(fun):
	def w2(*args,**kwargs):
		print ("参数",args)
		print("函数调用千的检查")
		fun(*args,**kwargs)
	return w2
@w1
def foo(*args,**kwargs):
	print("sotou")
	print("sotou参数",args)
	print("sotou参数",kwargs)
foo(5,6,6,5,4,3,32,2,a=5,o=9)







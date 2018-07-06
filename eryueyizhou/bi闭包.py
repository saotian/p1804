'''
def test(out):
	def test_1(out_1):
		print("内容是：%d"%out_1)
		return out_1+out
	return test_1


n = test(2)(1)
print(n)
'''
def wai(start=0):
	def nei():
		nonlocal start
		start +=1
		print(start)
		return ""
	return nei

a = wai(2)
a()
print("___________________")

def wai (a,b):
	def nei (x):
		print("%d*%d+%d"%(a,x,b))
		y = a*x+b
		return y
	return nei
w = wai(2,3)
print(w(4))























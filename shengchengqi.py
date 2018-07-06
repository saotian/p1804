'''
def shuliu(day):
	n = 0
	a,b = 0,1
	while n < day:
		yield (b)
		a,b = b,a+b
		n += 1
	return 'done'
q = shuliu(10)
for i in q:
	print (i)

def jishu(shu):
	n=0
	while n <= shu:
		n +=1
		if n%2 !=0:
			yield (n)
	return 'ok'
a = jishu(99)			
for i in a:
	print(i)
print()

def jishu(shu):
	n=0
	while n <= shu:
		n +=1
		if n%2 !=0:
			yield (n)
	return 'ok'
a = jishu(99)			
for i in a:
	print(i)


def oushu(shu):
	n=0
	while n <= shu:
		n +=1
		if n%2 ==0:
			yield (n)
	return 'ok'
a = oushu(99)
print(next(a))
print(next(a))
print(next(a))
print()
for i in a:
	print(i)
'''
for i in range (1,101):
print (i)	










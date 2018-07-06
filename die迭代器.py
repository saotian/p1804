from collections import Iterator
a = [x for x in range(1,101)]
c = iter(a)
print(isinstance(c,Iterator))
def shuliu(day):
	n = 0
	a,b = 0,1
	while n < day:
		yield (b)
		a,b = b,a+b
		n += 1
	return 'done'
q = shuliu(100)
for i in q:
	a.append(i)
print (a)(c,Iterator))


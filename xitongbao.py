list1=[]
def yinhang():
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("　银行管理系统".center(50," "))
	print("欢迎使用智能银行".center(50," "))
	print(' ')
	print(" ①　　　办　卡")
	print(" ②　　　存　钱")
	print(" ③　　　取　钱")
	print(" ④　　　查　询") 
	print(" ⑤　　　退　出")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def banka():
	dic1={}
	print(' ')
	name=str(input(" ◆  请输入你的名字---------- ："))
	age=int(input(" ◆  请输入你的年龄---------- ："))
	ldentity=int(input(" ◆  请输入你的身份证号------ ："))
	acc=int(input(" ◆  请输入你的银行卡号------ ："))
	pwd=int(input(" ◆  请输入你的银行卡密码---- ："))
	money=float(input(" ◆  请输入金额-------------- ："))
	dic1['acc']=acc
	dic1['pwd']=pwd
	dic1['money']=money
	dic1['name']=name
	dic1['age']=age
	dic1['ldentity']=ldentity
	list1.append(dic1)
	print(" ◆  办卡成功")
	print(list1)

def cunqian():
	print(' ')
	acc_1=int(input(" ◆  请输入银行账号----------："))
	pwd_1=int(input(" ◆  请输入银行密码----------："))
	for dic1 in list1:
		if acc_1 == dic1['acc']:
			if pwd_1 == dic1['pwd']:
				money=float(input(" ◆  请输入你要存入的金钱----："))
				dic1['money']=dic1['money']+money
				print(" ◆  余额--------------------：%0.2f"%(dic1['money']))
				print(' ◆  存钱成功')
				break
			else:
				print(" ◆  密码有误")
				break
	else:
		print(' ◆  账号有误')

def quqian():
	print(' ')
	acc_1=int(input(" ◆  请输入银行账号----------："))
	pwd_1=int(input(" ◆  请输入银行密码----------："))
	for dic1 in list1:
		if acc_1 == dic1['acc']:
			if pwd_1 == dic1['pwd']:
				money=float(input(" ◆  请输入你要取出的金钱----："))
				if money>dic1['money']:
					print(' ◆  你的余额不足')
					break
				else:
					dic1['money']=dic1['money']-money
					print(" ◆  余额--------------------：%0.2f"%(dic1['money']))
					print(' ◆  取钱成功')
					break
			else:
				print(" ◆  密码有误")
				break
	else:
		print(' ◆  账号有误')

def chaxun():
	print(' ')
	zhanghu=int(input(" ◆  请输入你要查找的账户----："))
	x=0
	for i in list1:
		if zhanghu==i['acc']:
			print(" ◆  名字:%s\n ◆  年龄:%s\n ◆  身份证号:%s\n ◆  银行账户:%s"%(i['name'],i['age'],i['ldentity'],i['acc']))
			x=1
	if x == 0:
		print(' ◆  没有此账户')
'''
while True:
	yinhang()
	gn=int(input(" ▶  请选择你要办理的业务----: "))
	if gn == 1:
		banka()
	elif gn == 2:
		cunqian()
	elif gn == 3:
		quqian()
	elif gn == 4:
		chaxun()
	elif gn == 5:
		print(" ")
	print(" ◆  退出成功,欢迎您下次使用")
	break
'''





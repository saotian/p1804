import xitongbao

while True:
	xitongbao.yinhang()
	gn=int(input(" ▶  请选择你要办理的业务----: "))
	if gn == 1:
		xitongbao.banka()
	elif gn == 2:
		xitongbao.cunqian()
	elif gn == 3:
		xitongbao.quqian()
	elif gn == 4:
		xitongbao.chaxun()
	elif gn == 5:
		print(' ')
		print('退出成功，欢迎您下次使用')
		break




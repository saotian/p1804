import os
class Wenjian():
	def mingpian():
		print("名片系统".center(50," "))
		print("欢迎使用名片系统".center(50," "))
		print("  ")
		print("1.写文件")
		print("2.读文件")
		print("3.备份文件")
		print("4.重命名文件")
	def xie():
		name = input("请输入你要写的文件名")
		f = open(name,"w")
		w = input("请输入你要加入的内容")
		f.write(w)
		f.close
	def du():
		name = input("请输入你要读的文件名")
		f = open(name,"r")
		b = f.read()
		print(b)
	def beifen():
		name = input("请输入你要备份的文件名")
		f = open(name,"r")
		position = name.rfind(".")
		new_name = name[:position]+"back"+name[position:]
		f1 = open(new_name,"w")
		q = f.read()
		f1.write(q)
		f.close()
		f1.close()
	def chongmingming():
		dir_name = input("请输入文件夹名字") 
		diles = os.listdir(dir_name) 
		for i in diles: 
			a = i.rfind(".") 
			new_name = i[:a]+"精品"+i[a:] 
			old_name = dir_name+"/"+i 
			new_name = dir_name+"/"+new_name 
			os.rename(old_name,new_name)

def gongneng():
	while True:
		mingpian()
		a = input("请输入功能:")
		if a == "1":
			b.xie()
		elif a == "2":
			b.du()
		elif a == "3":
			b.beifen()
		elif a == "4":
			b.chongmingming()
		else:
			break

b = Wenjian()
b.gongneng()
















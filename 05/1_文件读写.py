name = input("请输入要备份的文件名字")
f = open(name,"r")

position = name.find(".")
newname = name[:position]+"back"+name[position:]
f1 = open(newname,"w")
while True:
	content = f.read(1024)
	f1.write(a)
	if f.read == "":
		break


a = f.read()
nename.write(a)

f.close()
newname.close()

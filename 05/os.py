import os
dir_name = input("请输入文件夹名字")
diles = os.listdir(dir_name)
for i in diles:
	a = i.rfind(".")
	new_name = i[:a]+"精品"+i[a:]
	old_name = dir_name+"/"+i
	new_name = dir_name+"/"+new_name
	os.rename(old_name,new_name)

# os.rename(i,new_name)     第二种

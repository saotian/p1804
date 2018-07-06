import time
class Digua():
    def __init__(self):
        self.zt = '生的'
        self.time = 0
        self.list=[]
    def cook(self):
        self.time += 1
        if self.time < 2:
            self.zt = '生的'
        elif self.time >=2 and self.time < 5:
            self.zt = '半生不熟'
        elif self.time >=5 and self.time < 10:
            self.zt = '熟了'
        elif self.time > 10:
            self.zt = '烤糊了'
    def aa(self):
        print(self.zt)
        print("作料有%s"%str(self.list))
    def addZuoLiao(self,s):
        self.list.append(s)
digua = Digua()
for i in range (8):
    digua.cook()
    if i == 1:
        digua.addZuoLiao('盐')
    elif i == 3:
        digua.addZuoLiao('糖')
    elif i == 5:
        digua.addZuoLiao('麻油')
    digua.aa()
    time.sleep(1)











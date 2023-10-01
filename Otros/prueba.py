from Nivel1.Otros.raro import medir
import matplotlib.pyplot as plt
def metodo1(arg):
    return [i**3 for i in range(arg)]

def metodo2(arg):
    L=[]
    for i in range(arg):
        L.append(i**3)
    return L

rs = [10**i for i in range(1,8)]
ldt=[]
ldt2=[]
for i in rs:
    delta, res = medir(i,metodo1)
    ldt.append(delta)
    delta2, res2 = medir(i,metodo2)
    ldt2.append(delta2)
plt.plot(rs,ldt)
plt.plot(rs,ldt2)
plt.show()

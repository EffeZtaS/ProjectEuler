from Nivel1.Otros.raro import medir
import matplotlib.pyplot as plt
def metodo1(arg):
    suma=0
    for i in range(arg):
        if i%3==0 or i%5==0:
            suma+=i
    return suma

def metodo2(arg):
    lis=[i if (i%3==0 or i%5==0) else 0 for i in range(arg)]
    return sum(lis)

def metodo3(arg):
    val=0
    for i in range(arg):
        val+=i if (i%3==0 or i%5==0) else 0
    return val

def metodo4(arg):
    val=0
    k=1
    while k<arg:
        if (k%3==0 or k%5==0):
            val+=k
        k+=1
    return val
def metodo5(arg):
    L1=[i*3 for i in range(arg//3+1)]
    L2=[i*5 for i in range(arg//5)]
    L3=list(set(L1).intersection(L2))
    return sum(L1)+sum(L2)-sum(L3)

def metodo6(arg):
    sd3= 3*int(arg/3)*(arg//3+1)/2
    sd5= 5*int(arg/5-1)*(arg//5)/2
    sd15= 15*int(arg/15)*(arg//15+1)/2
    return int(sd3+sd5-sd15)

LdF = [metodo1, metodo2, metodo3, metodo4, metodo5, metodo6]
LdTs=[]
LdA=[10**i for i in range(1,6)]
LdR=[]
for k in LdF:
    LdT=[]
    for i in LdA:
        delta, res = medir(i,k)
        LdT.append(delta)
        print(res)
    LdTs.append(LdT)

for idx, i in enumerate(LdTs):
    plt.plot(LdA,i)
    plt.legend('metodo'+str(idx+1))
plt.show()
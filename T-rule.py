#coding: utf-8
import numpy as np
def f(x):
	return float((2 * ((np.exp(x ** 2)) ) * x) ** 0.5)


a=0
b=1
n=4
h=float((b-a))/float(n)
print('a=%f b=%f h=%f' %(a,b,h))
x=np.array(np.arange(a,b+h,h))
print(x)
soma=0
for i in range(1,n):
	soma+= 2*f( x[i] )

intt = float(h/2)*(f(x[a]) + soma + f(x[b])) 
print(intt)


import numpy as np
import matplotlib.pyplot as plt

def funcion(t,v):
    g=9.81
    c=12.5
    m=68.1
    ec=g-c/m*v
    return ec

h=0.1
s=10

n=int((s/h)+1)
print(n)
t=np.zeros(n)
v=np.zeros(n)


print(t[0],v[0])
for i in np.arange(1,n):
    v[i]=v[i-1]+h*funcion(t[i-1],v[i-1])
    t[i]=t[i-1]+h

    print(t[i],v[i])

plt.plot(t,v)

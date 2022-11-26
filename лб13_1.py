import math 

 

import numpy as np 

 

import matplotlib.pyplot as plt 

 

def f(x,y): 

 

    return x + math.sin(y/3) 

 

x0 = 1.6 

 

b=2.6 

 

h = 0.1 

 

x=np.arange(x0,b+h,h) 

x=np.arange(x0,b+h,h) 

 

n=len(x)-1 

 

y=np.empty(n+1) 

 

y[0]= 4.6 

 

for i in range(n): 

 

    y[i+1]=y[i]+(f(x[i],y[i])+f(x[i+1],y[i]+h*f(x[i],y[i])))*h/2 

 

    y_rounded=np.round_(y,4) 

 

print('x=',x, '\ny=',y_rounded) 

 

plt.plot(x, y, 'o',x,y,'red') 

 

plt.xlabel('x') 

plt.ylabel('y') 

 

plt.title('Mетод Eйлeра-Коші') 

plt.legend([]) 

plt.grid() 

plt.show() 

 

n=len(x)-1 

 

y=np.empty(n+1) 

 

y[0]= 4.6 

 

for i in range(n): 

 

    y[i+1]=y[i]+f(x[i],y[i])*h 

 

    y_rounded=np.round (y,4) 

 

print('x=',x, '\ny=',y_rounded) 

 

plt.plot(x, y, 'o',x,y,'red') 

 

plt.xlabel('x') 

plt.ylabel('y') 

 

plt.title('Mетод Eйлeра') 

plt.legend([]) 

plt.grid() 

plt.show() 

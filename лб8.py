import numpy as np 

from math import factorial 

import matplotlib.pyplot as plt 

 

 

x=[0.101,0.106,0.111,0.116,0.121,0.126,0.131,0.136] 

y=[1.2618,1.2764,1.2912,1.3061,1.3213,1.3366,1.3520,1.3677] 

h = x[1] - x[0] 

x1=0.104 

x2=0.133 

q=(x1 - x[0])/h #Для 1 інтерп. ф-ли Нтютона 

q1 = (x2-x[7])/h #Для 2 інтерп. ф-ли Нтютона 

def n(y,j): #обчислення кінцевих різниць 

    mas=[] 

    for i in range(len(y)): 

        mas.append(y[i] - y[i-1]) 

    mas.pop(0)   

    if j == 1: 

        return mas 

    else: 

        j-=1 

        return n(mas, j) 

 #Перша інтерполяційна формула Ньютона    

s_1 = y[0]+q*n(y,1)[0]+q*(q-1)*n(y,2)[0]/factorial(2) 

s_2 = q*(q-1)*(q-2)*n(y,3)[0]/factorial(3) 

s_3 = q*(q-1)*(q-2)*(q-3)*n(y,4)[0]/factorial(4) 

s_4 = q*(q-1)*(q-2)*(q-3)*(q-4)*n(y,5)[0]/factorial(5) 

n_1 = s_1 + s_2 + s_3 + s_4 

 

#Спроба обчислити n_1 через цикл 

#n_1=y[0]  

#for  k in range(len(y)): 

#    prod = (q-k)*n(y,k+1)[0]/factorial(k+1) 

#    n_1=n_1 + q*prod 

print ('The value of a function at a point x1=', x1, 'using Newton*s First Interpolation Formula', round(n_1,5)) 

 

#Друга інтерполяційна формула Ньютона 

#Додати код 

t1 = y[5] + q1*n(y,1)[4]+q1*(q1+1)*n(y,2)[3]/factorial(2) 

t2 = q1*(q1+1)*(q1+2)*n(y,3)[2]/factorial(3) 

t3 = q1*(q1+1)*(q1+2)*(q1+3)*n(y,4)[1]/factorial(4) 

t4 = q1*(q1+1)*(q1+2)*(q1+3)*(q1+4)*n(y,4)[1]/factorial(5) 

n_2 =  t1+t2+t3+t4 

#Можна спробувати написати цикл 

print ('The value of a function at a point x2=', x2, 'using Newton*s Second Interpolation Formula', round(n_2,5)) 

 

x_1=np.linspace(np.min(x), np.max(x)) 

y_1=np.linspace(np.min(y), np.max(y)) 

plt.plot(x,y, 'ro', x_1, y_1) 

plt.title('Graph of the interpolation function') 

plt.xlabel('x') 

plt.ylabel('y') 

plt.grid() 

plt.show() 

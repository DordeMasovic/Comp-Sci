# chebychev with differential equation
from numpy import *
h=0.05

def func(x,n):
    return (1-x*x)*n*n*cos(n*pi/2) - x*n*sin(n*pi/2) + n*n*cos(n*pi/2)



def f1(x,n):
    return func(x,n)
    
def f2(x,n):
    return func(x+0.5*h*f1(x,n),n)
    
def f3(x,n):
    return func(x+0.5*h*f2(x,n),n)
    
def f4(x,n):
    return func(x+0.5*h*f3(x,n),n)

x0 = 0
n=2
y = [0]
x1 = h*(f1(x0,n)+2*f2(x0,n)+2*f3(x0,n)+f4(x0,n))/6.
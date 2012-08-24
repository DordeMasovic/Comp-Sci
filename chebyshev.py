from numpy import *
from matplotlib import *
from pylab import *


def fpoint(f,a,b,B=20):
    bereich = (b-a)/(float(B))
    c4 = 1375/576.
    c2 = 125/144.
    c0 = 335/96.
    int=0
    for i in range(0,B):
        x=linspace(a+i*bereich,a+(i+1)*bereich,11)
        int+=(c4*f(x[5-4])+c2*f(x[5-2])+c0*f(x[5])+c2*f(x[5+2])+c4*f(x[5+4]))*(b-a)/(10*B)
    return int

def evalp(c,x):
    n = len(c)-1
    sum = c[-1]
    for k in range(n,0,-1):
        sum = x*sum+c[k-1]
    return sum

# n is the number of polynomial that I wish
n = 6

# generating a bunch of polynomial 1,x^2,x^3,x^4 and so on
poly = []
for i in range(n):
    p = zeros(i+1,float)
    p[i] = 1.
    poly.append(p)

# gram-schmidt orthonormalization for all polynomial in the array poly
for i in range(len(poly)):             
    for j in range(len(poly[i])-1):   
        for k in range(len(poly[j])):
                poly[i][k] -= fpoint(lambda x: (evalp(poly[i],x)*evalp(poly[j],x))/(sqrt(1-x*x)),-1,1)*poly[j][k]
    betrag = fpoint(lambda x: (evalp(poly[i],x)*evalp(poly[i],x)/(sqrt(1-x*x))),-1,1)
    poly[i] = poly[i]/sqrt(betrag)

# generating the Chebyshev polynom with multiplication with the factor sqrt(pi/2)
for i in range(1,len(poly)):
    poly[i] = sqrt(pi/2)*poly[i]
# this is the exception for that m=n=0 it have to get pi
poly[0] = poly[0]*sqrt(pi)

# make a nice plot
xachse = linspace(-1,1,50)
for i in range(len(poly)):
    y = map(lambda x: evalp(poly[i],x),xachse)
    plot(xachse,y)
show()




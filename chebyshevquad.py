from numpy import *
from matplotlib import *
from pylab import *


# using a new method to integrate from 0 to pi with the gaussquadratur
def gaussquadr(f,M):
    inter = 0
    for k in range(int(M)):
        inter += f(cos((k-0.5)*pi/M))    
    return pi*inter/M

def evalp(c,x):
    n = len(c)-1
    sum = c[-1]
    for k in range(n,0,-1):
        sum = x*sum+c[k-1]
    return sum

# n is the number of polynomial that I wish
n = 8
# M is the number of the evaluation
M = 150.

# generating a bunch of array with 1 at the point i
poly = []
for i in range(n):
    p = zeros(i+1,float)
    p[i] = 1.
    poly.append(p)

# gram-schmidt orthonormalization for all polynomial in the array poly
for i in range(len(poly)):             
    for j in range(len(poly[i])-1):   
        for k in range(len(poly[j])):
                poly[i][k] -= gaussquadr(lambda x: (evalp(poly[i],x)*evalp(poly[j],x)),M)*poly[j][k]
    betrag = gaussquadr(lambda x: (evalp(poly[i],x)*evalp(poly[i],x)),M)
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




# three body problem, Dorde Masovic

from numpy import *
from scipy.integrate import *
from pylab import *

mu=0.25

# the derivat of the potential to x
def dvdx(v):
    x,y,px,py = v
    return (1-mu)*(x+mu)**2 / ((x+mu)**2 + y**2)**(3/2.) + mu*(x-1+mu) / ((x-1+mu)**2 + y**2)**(3/2.)

# derivation of the potential to y
def dvdy(v):
    x,y,px,py = v
    return (1-mu)*y / ((x+mu)**2 + y**2)**(3/2.) + mu*y / ((x-1+mu)**2 + y**2)**(3/2.)
    
# differential equations for x,y,px,py
def threebody(v,t):
    x,y,px,py = v
    return [ px+y , py-x , py-dvdx(v) , -(px+dvdy(v))  ]
    
# timeline
t = linspace(0,20,10000)
# initial conditions
v = [0.5,1.6,0,0]

res = odeint(threebody, v , t)
plot(res[:,0],res[:,1])
show()

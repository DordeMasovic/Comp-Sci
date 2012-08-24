from numpy import *
from time import time
from pylab import *
import math


t = int(time())-1300708800
delta = 2*pi/(365.*24.*3600.)
sigma = 2*pi/(24.*3600.)
lat = linspace(-pi/2.,pi/2.,1000)
lon = linspace(-180,180,100)
erdink = radians(-23.4385)

def sunpos(t):
    return [cos(delta*t),sin(delta*t)*cos(erdink),sin(delta*t)*sin(erdink)]
    
def zenith(t,l):
    return [cos(l)*cos((sigma+delta)*t+l),cos(l)*sin((delta+sigma)*t+l),sin(l)]

def betrag(x):
    return sqrt(sum(x*x))
    
def scoord(x):
    phi = math.atan2(x[1],x[0])
    theta = math.acos( x[2] / betrag(x) )
    return array([degrees(phi),degrees(theta-pi/2.)])

def karcoord(x,y):
    return array([sin(x)*cos(y), sin(x)*sin(x),cos(x)])

sun = array(sunpos(t))
di = []
N=10
for j in range(0,N):
    for i in lat:
        dire = array(zenith(t,i))
        ang = (sum(dire*sun))/(betrag(sun)*betrag(dire))
        if (abs(ang-pi*j/(2.*N))<=0.01):
            winkel = scoord(dire)
            di.append(winkel)
            plot(winkel[0],winkel[1],'o')
            
sun = scoord(sun)
plot(sun[0],sun[1],'o')
show()
        
print di
    
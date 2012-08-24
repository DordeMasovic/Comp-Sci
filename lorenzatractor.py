# lorenz atractor, Masovic Dorde

from numpy import *
from scipy.integrate import *
from pylab import *
from Canvas import *
from Tkinter import *
import time

sigma = 10.
r = 28.
b = 8/3.

def lorenz(v,t):
    x,y,z = v
    return [ sigma*(y-x) , r*x-y-x*z , x*y-b*z ]


screen = Tk()
wd,ht = screen.winfo_screenwidth(),screen.winfo_screenheight()
screen.geometry("%dx%d+0+0"%(wd,ht))
canv = Canvas(screen,height=ht,width=wd,background="black")
canv.pack()
#update()
t = linspace(0,50,10000)
v = [1.,0,0]
res = odeint(lorenz,v,t)
x = res[:,0]
y = res[:,1]

xo = x[0]
yo = y[0]
for i in range(1,len(res[:,0])-1):
    xn = 13*x[i]
    yn = 13*y[i]
    canv.create_line(int(xo+wd/2.),int(yo+ht/2.),int(xn+wd/2.),int(yn+ht/2.),fill='red')
    time.sleep(0.01)
    xo = xn
    yo = yn
screen.mainloop()




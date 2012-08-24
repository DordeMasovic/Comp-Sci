# lorenz atractor, Masovic Dorde

from numpy import *
from scipy.integrate import *
from pylab import *
from Canvas import *
from Tkinter import *

sigma = 10.
r = 28.
b = 8/3.

def lorenz(v,t):
    x,y,z = v
    return [ sigma*(y-x) , r*x-y-x*z , x*y-b*z ]

t = linspace(0,50,10000)
v = [5,5,0]
res = odeint(lorenz,v,t)
plot(res[:,0],res[:,1])
show()

i = 0



screen = Tk()
wd,ht = screen.winfo_screenwidth(),screen.winfo_screenheight()
screen.geometry("%dx%d+0+0"%(wd,ht))
canv = Canvas(screen,height=ht,width=wd,background="black")
canv.pack()
update()
screen.mainloop()




# schroedinger, Dorde Masovic
from numpy import *
from scipy import *
from pylab import *
from Tkinter import * 
from Canvas import *
from matplotlib import *

# define my axis in the real room
x = linspace(-4.5,4.5,600)
# transform the real axis in to the k-room
k = fft(x)

# definition to calculat the kinetic energie in the k-room
def B(k,t):
    return exp(t*complex(0.,1.)*k*k/2.)

 # definition to calculate the potential in the real room
def pot(x):
    return pow(abs(x*x-1),2)/2.
def A(x,t):
    return exp(t*complex(0.,1.)*(pot(x))/2.)

screen = Tk()
wd,ht = screen.winfo_screenwidth(),screen.winfo_screenheight()
screen.geometry("%dx%d+0+0"%(wd,ht))
canv = Canvas(screen,height=ht,width=wd,background="black")
canv.pack()

# some scale factor to enlarge the animation
scaley = 150
scalex = 140

# define the time
for t in linspace(0.1,0.5,2000):
#    calculate A and B
    expA = map(lambda x: A(x,t),x)
    expB = map(lambda k: B(k,t),k)

#    tranform back the k-room into the real room
    expB = ifft(expB)
#    calculate the time depended hamiltonien
    y = expA*expB*expA
# i took the norm of phi because thr numbers get realy large with t
    y = real(y)/max(abs(real(y)))
# draw the waves with lines
    for i in range(len(y)-1):
        y0=y[i]
        y1=y[i+1]
        x0=x[i]
        x1=x[i+1]
        canv.create_line(scalex*x0+650, 400+scaley*y0, scalex*x1+650, 400+scaley*y1,fill='red')
    canv.update()
    canv.delete(ALL)

screen.mainloop()
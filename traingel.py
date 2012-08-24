from Tkinter import *
from Canvas import *
from matplotlib import *

global a,b,c,x0,y0
size = 300

# inital coord for the triangle-----------------------------------------------
a = complex(20,size-20)
b = complex(size-20,size/2)
c = complex(20,20)

# now come a lot of def

# def to draw a triangle with lines---------------------------------------------
def trian(a,b,c):
    canv.create_line(a.real,a.imag,b.real,b.imag)
    canv.create_line(b.real,b.imag,c.real,c.imag)
    canv.create_line(c.real,c.imag,a.real,a.imag)


# def when i click and move button-1, it catch the new coord and draw a new triangle
# it check witch corner is nearest to the clickpoint and take it for the new coord.
def clicked(event):
    global x0,y0,a,b,c
    x0 = event.x
    y0 = event.y
    newcoord=complex(x0,y0)
    canv.delete(ALL)
    if (abs(a-newcoord)<abs(b-newcoord)) and (abs(a-newcoord)<abs(c-newcoord)):
        trian(newcoord,b,c)
        a=newcoord
    elif (abs(b-newcoord)<abs(a-newcoord)) and (abs(b-newcoord)<abs(c-newcoord)):
        b=newcoord        
    else: 
        c=newcoord
    trian(a,b,c)

    
# gamma is the faktor for the line between p and (b+a)/2
# beta is the factor in the line equation ac
# alpha is the factor in the line equation bc
# this are faktor of the equation for gamma,beta and alpha --------------------
def formula(a,b,c,p):
    return ( (c-a) , (-1.)*( p-(b+a)/2.) , p - a )
    
def formula2(a,b,c,p):
    return ( (c-b) , (-1.)*( p-(b+a)/2.) , p - b )


# this def solve me and give back gamma, beta or alpha--------------------------
def eqsyst(reel,imag):
    reel = (reel[0]-imag[0]*reel[1]/imag[1] , 0 , reel[2] - imag[2] * reel[1]/imag[1])
    reel = (1,0,reel[2]/reel[0])
    imag = (0,1, (imag[2]-reel[2]*imag[0])/imag[1])
    return (reel[2],imag[2])


# her i initial all the calculation for gamma,beta and alpha -------------------   
def faktor(p):
    reel = formula(a.real,b.real,c.real,p.real)
    imag = formula(a.imag,b.imag,c.imag,p.imag)
    beta_gamma = eqsyst(reel,imag)
    
    reel = formula2(a.real,b.real,c.real,p.real)
    imag = formula2(a.imag,b.imag,c.imag,p.imag)
    alpha_gamma = eqsyst(reel,imag)
    
    return (beta_gamma,alpha_gamma)


# in this definition is the repaint of the triangle and the decision if is a --
# green or red dot
def clicked_point(event):
    canv.delete(ALL)
    trian(a,b,c)
    x0 = event.x
    y0 = event.y
    p = complex(x0,y0)
    x = faktor(p)
    if (( 1>= x[0][0] >=0) and (x[0][1]>=0)):
        canv.create_oval(x0-4,y0-4,x0+4,y0+4,fill='green')
    else:
        if (( 1>= x[1][0] >=0) and (x[1][1]>=0)):
            canv.create_oval(x0-4,y0-4,x0+4,y0+4,fill='green')
        else:
            canv.create_oval(x0-4,y0-4,x0+4,y0+4,fill='red')
    

root = Tk()
canv = Canvas(root,width=size,height=size)
trian(a,b,c)
canv.bind("<Button-1>",clicked_point)
canv.bind("<B1-Motion>",clicked)
canv.pack()
root.mainloop()


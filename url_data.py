# -*- coding: utf-8 -*-
# read out internet webside, Dorde Masovic

from urllib import *
from pylab import *

fil = urlopen("http://www.wwis.dwd.de/087/c00312.htm")
src = fil.read()
# I want to read out the minimal and maximal temperatur for every month
min=[]
max=[]


monate=["Januar","Februar","März","April","Mai","Juni","Juli","August","September","Oktober","November","Dezember"]

# I split the text to every monthname, from there i search for the color in front
# of the number and the other stuff behind the number. In this way i isolate the
# number at the end
for i in range(0,len(monate)):
    splittext = src.partition(monate[i])
    splittext = splittext[2].partition('color="#0000FF">')
    splittext = splittext[2].partition("</font></b></td>")
    try:
        min.append(float(splittext[0]))
    except:
        min.append(0)
        
    splittext = splittext[2].partition('color="#FF0000">')
    splittext = splittext[2].partition("</font></b></td>")
    try:
        max.append(float(splittext[0]))
    except:
        max.append(0)

# try to make a nice bar plot
fig = plt.figure()
ax = fig.add_subplot(111)
statist2=ax.bar(range(12),max,width=1,color='r')
statist1=ax.bar(range(12),min,width=1,color='b')
ax.set_xlabel("Month number")
ax.set_ylabel("Temperatur")
ax.legend( (statist1[0], statist2[0]), ('Minimal', 'Maximal') )
show()


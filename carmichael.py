# -*- coding: utf-8 -*-
# read out internet webside, Dorde Masovic

from urllib import *
from pylab import *

# because my sieve is not very good and not very fast I read the prime number from a
# webside
fil = urlopen("http://primzahlen.zeta24.com/de/primzahltabelle10000.php")
src = fil.read()

splittext = src.partition("<div class='proofbox'>")
splittext = splittext[2].partition("<p style='font-size:10px;'> ")
splittext = splittext[2].partition('</p>')
primnumber = splittext[0]


N=100
odd=map(lambda x: 2*x + 1 , range(1,N))
print odd
    





carmichael=[]
for i in range(4,4000):
    if ((pow(4,i-1,i)==1)) :
        try:
            x=primnumber.index(str(i))
        except:
            carmichael.append(i)
print carmichael



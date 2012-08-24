# -*- coding: utf-8 -*-
# generate Carmichael numbers, Dorde Masovic

from pylab import *

# generate a list of prime number from 3 to 2*N+1
N=2000
prime = range(3,2*N+1,2)
j=0
while j <= int(sqrt(N)): # ok, this isn't nice but its work fast
    try:
        l=len(prime)-1
        while prime[j]!= prime[l]:
            if prime[l]%prime[j]==0:
                prime.remove(prime[l])
            l-=1
        j+=1
    except:
        j+=1
prime.insert(0,2)
# print prime

# Now i search for Carmichael numbers
carmichael2=[]
# Carmichael are odd numbers, mayby it's faster when i use only odd number
# and its enough to look if a number is divided by prime because every other
# number is a product of primenumbers
for i in range(1,2*N+1,2):  
    j=0
    x=0
    while prime[j]<=i:
        if (prime[j]!=i):                        # check if its a prime number
            if ((i%prime[j]!=0)):                # for every number thats not a divider, thats the definition of fermats little theorem 
                if ((pow(prime[j],i-1,i)==1)):   # it have to fulfill fermats little theorem
                    x=1
                else:
                    x=0
                    break
        else:
            x=0
            break
        j+=1
    if x:
        carmichael2.append(i)
print carmichael2



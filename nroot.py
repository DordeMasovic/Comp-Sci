def nroot(x,n): # n-th root of x > 0
    yn0 = x / 3.  # initialize the begin 
    yn0_old = x
    while abs(yn0_old - yn0) > 0 :
        yn0_old = yn0
        yn0 = yn0 - (pow(yn0,n)-x)/(n*pow(yn0,n-1))
        print "yn0 :", yn0
    print 'the ',n,'th-root of ',x,' is: ',yn0

    
# main program, i wrote in this way to be able to open it and type the numbers
print('x:') 
x = input()
print('n-th root:')
n = input()
nroot(x,n)
input()
    
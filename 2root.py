def nroot(x): 
# n-th root of x > 0
    yn0 = x / 2.
    yn0_old = x
    while abs(yn0_old - yn0) > 0 :
        yn0_old = yn0
        yn0 = ( (n-1)*yn0 / n ) - ( x /(n*pow(yn0,n-1)) )
    print("the ", n,"root is:",yn0)
    
# main program
nroot(5,2)
input()
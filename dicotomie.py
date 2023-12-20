

def di(f,a,b,d=1e-16):
    
    while b-a>d :
        #print(a,b)
        c=(a+b)/2
        if f(a)*f(c) >0:
            a=c
        else:
            b=c 
    return c  

def f(x):
    return x ** 2 - 2
print(di(f,1,2,d=1e-15))
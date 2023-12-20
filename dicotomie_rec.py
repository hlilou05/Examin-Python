def di(f,a,b,d=1e-16):
   if b - a < d :
       return a
   x = (a + b)/2
   if f(a)*f(x) < d:
       return di(f,a,x,d)
   else :
       return di(f,x,b,d)
   
def g(x):
    return x ** 2 - 2
print(di(g,1,2))